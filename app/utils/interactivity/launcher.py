"""Algorithm launcher with execution timing and result display."""

import json
from pathlib import Path
from typing import Any, Dict, Tuple

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from app.exercises import ExerciseManager
from app.utils.logging.logging_config import get_logger

console = Console()
logger = get_logger(__name__)


class AlgorithmLauncher:
    """Handles algorithm execution with timing and result display."""

    def __init__(self, data_file: str = "source.json") -> None:
        """Initialize launcher with data file.
        
        Args:
            data_file: Path to JSON data file.

        """
        self.data_file = Path(data_file)
        self.data: Dict[str, Any] = {}
        logger.debug(f"Launcher initialized with data file: {data_file}")

    def load_data(self) -> None:
        """Load data from JSON file."""
        try:
            with open(self.data_file, encoding="utf-8") as f:
                self.data = json.load(f)
            logger.debug(f"Data loaded successfully from {self.data_file}")
        except FileNotFoundError:
            logger.error(f"Data file not found: {self.data_file}")
            console.print(f"[red]Erreur: Fichier {self.data_file} introuvable[/red]")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {self.data_file}: {e}")
            console.print(f"[red]Erreur JSON dans {self.data_file}: {e}[/red]")
            raise

    def execute_algorithm(self, command: str, debug: bool = False) -> Tuple[Any, float]:
        """Execute the specified algorithm with timing.
        
        Args:
            command: Algorithm command to execute.
            debug: Enable debug mode.
            
        Returns:
            Tuple of (result, execution_time_ms).

        """
        algo_type = ExerciseManager.get_by_command(command)
        if not algo_type:
            raise ValueError(f"Algorithme non trouvé: {command}")

        info = ExerciseManager.get_algorithm_info(algo_type)

        if debug:
            logger.debug(f"Executing algorithm '{info.name}' in debug mode")

        console.print(f"\n[bold blue]🚀 Lancement: {info.name}[/bold blue]")
        console.print(f"[dim]{info.exercise}[/dim]\n")

        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
            transient=True,
        ) as progress:
            task = progress.add_task("Exécution en cours...", total=None)

            try:
                result, exec_time = ExerciseManager.execute_algorithm(algo_type, self.data)
                progress.update(task, description="[green]✓ Terminé![/green]")
                return result, exec_time
            except Exception as e:
                progress.update(task, description="[red]✗ Erreur![/red]")
                logger.error(f"Algorithm execution failed: {e}")
                raise

    def display_results(self, result: Any, exec_time: float, command: str) -> None:
        """Display algorithm results in a formatted way.
        
        Args:
            result: Algorithm execution result.
            exec_time: Execution time in milliseconds.
            command: Algorithm command for display.

        """
        algo_type = ExerciseManager.get_by_command(command)
        if algo_type:
            info = ExerciseManager.get_algorithm_info(algo_type)
            title = info.name
        else:
            title = command.upper()

        # Create results panel
        result_text = self._format_result(result)
        time_text = f"[green]⏱️  Temps d'exécution: {exec_time:.2f} ms[/green]"

        panel_content = f"{result_text}\n\n{time_text}"

        console.print(Panel(
            panel_content,
            title=f"[bold]Résultats - {title}[/bold]",
            border_style="green",
        ))

    def _format_result(self, result: Any) -> str:
        """Format result for display.
        
        Args:
            result: Result to format.
            
        Returns:
            Formatted result string.

        """
        if isinstance(result, dict):
            lines = []
            for key, value in result.items():
                lines.append(f"[yellow]{key}:[/yellow] {value}")
            return "\n".join(lines)
        if isinstance(result, (list, tuple)):
            return f"[cyan]Résultat:[/cyan] {' → '.join(map(str, result))}"
        if isinstance(result, str) and "Exercice" in result:
            # Handle placeholder results
            return f"[cyan]{result}[/cyan]"
        return f"[cyan]Résultat:[/cyan] {result}"

    def run(self, command: str, debug: bool = False) -> None:
        """Run complete algorithm execution pipeline.
        
        Args:
            command: Algorithm command to execute.
            debug: Enable debug mode.

        """
        try:
            self.load_data()
            result, exec_time = self.execute_algorithm(command, debug)
            self.display_results(result, exec_time, command)
        except Exception as e:
            console.print(f"[red]Erreur lors de l'exécution: {e}[/red]")
            if debug:
                raise
