"""Interactive menu system using Rich for the algorithm toolbox."""


from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.text import Text

from app.exercises import ExerciseManager
from app.utils.logging.logging_config import get_logger

console = Console()
logger = get_logger(__name__)


class AlgorithmMenu:
    """Interactive menu for selecting and running algorithms."""

    def __init__(self) -> None:
        """Initialize the menu with algorithm categories."""
        self.algorithms = ExerciseManager.get_by_category()
        logger.debug("Menu initialized with algorithm categories")



    def display_menu(self) -> None:
        """Display the interactive menu with all algorithms."""
        table = Table(
            title="Algorithmes Disponibles",
            show_header=True,
            header_style="bold magenta",
        )
        table.add_column("Catégorie", style="cyan", width=20)
        table.add_column("État", style="white", width=5, justify="center")
        table.add_column("Commande", style="green", width=15)
        table.add_column("Nom", style="yellow", width=30)
        table.add_column("Description", style="white", width=50)
        table.add_column("Paramètres utilisées", style="white", width=50)

        for category, algos in self.algorithms.items():
            for i, algo in enumerate(algos):
                info = ExerciseManager.get_algorithm_info(algo)

                # Check if algorithm is implemented
                is_implemented = ExerciseManager.is_algorithm_available(algo)
                status_icon = "✓" if is_implemented else "✗"
                status_style = "green" if is_implemented else "red"

                category_name = category if i == 0 else ""

                table.add_row(
                    category_name,
                    Text(status_icon, style=status_style),
                    info.command,
                    info.name,
                    info.description,
                    ", ".join(info.parameters) if info.parameters else "Aucun",
                )

            # Add separator except for last category
            if category != list(self.algorithms.keys())[-1]:
                table.add_row("", "", "", "", "")

        console.print(table)

        # Add legend
        legend = (
            "[dim]Légende: [green]✓[/green] Implémenté | "
            "[red]✗[/red] Non implémenté | "
            "[yellow]quit[/yellow] Quitter[/dim]"
        )
        console.print(f"\n{legend}")

    def get_user_choice(self) -> str:
        """Get user's algorithm choice with validation."""
        # Get implemented algorithms only for choices
        all_commands = ExerciseManager.get_all_commands()
        implemented_commands = [
            cmd for cmd in all_commands
            if ExerciseManager.is_algorithm_available(
                ExerciseManager.get_by_command(cmd),
            )
        ]

        valid_choices = implemented_commands + ["quit", "help", "list"]

        while True:
            choice = Prompt.ask(
                "\n[bold]Choisissez un algorithme[/bold] "
                "(ou 'quit' pour quitter, 'help' pour aide, 'list' pour lister)",
                default="quit",
            )

            if choice in ["quit", "help", "list"]:
                return choice

            if choice in all_commands:
                algo_type = ExerciseManager.get_by_command(choice)
                if not ExerciseManager.is_algorithm_available(algo_type):
                    console.print(
                        f"[red]⚠️  L'algorithme '{choice}' n'est pas encore implémenté[/red]",
                    )
                    continue
                return choice

            console.print(
                f"[red]❌ Commande invalide: '{choice}'. "
                f"Tapez 'list' pour voir les commandes disponibles.[/red]",
            )

    def show_help(self) -> None:
        """Display help information."""
        help_text = """
[bold blue]Aide - Boîte à Outils Algorithmique[/bold blue]

[yellow]Commandes disponibles:[/yellow]
• [green]<algorithme>[/green] - Exécuter un algorithme spécifique
• [green]help[/green] - Afficher cette aide
• [green]list[/green] - Lister tous les algorithmes par catégorie
• [green]quit[/green] - Quitter l'application

[yellow]Utilisation en ligne de commande:[/yellow]
• [dim]python -m app.main[/dim] - Mode interactif (ce menu)
• [dim]python -m app.main <algorithme>[/dim] - Exécution directe
• [dim]python -m app.main --debug <algorithme>[/dim] - Avec logs détaillés

[yellow]Exemples:[/yellow]
• [dim]python -m app.main dfs[/dim]
• [dim]python -m app.main --debug dijkstra[/dim]
• [dim]python -m app.main bfs-connexe[/dim]
        """
        console.print(Panel(help_text.strip(), border_style="blue"))

    def list_algorithms_by_category(self) -> None:
        """Display algorithms organized by category with implementation status."""
        for category, algos in self.algorithms.items():
            console.print(f"\n[bold cyan]📁 {category}[/bold cyan]")

            for algo in algos:
                info = ExerciseManager.get_algorithm_info(algo)
                is_implemented = ExerciseManager.is_algorithm_available(algo)

                status = "[green]✓[/green]" if is_implemented else "[red]✗[/red]"
                console.print(f"  {status} [yellow]{info.command}[/yellow] - {info.name}")
                console.print(f"    [dim]{info.description}[/dim]")

    def show_algorithm_details(self, command: str) -> None:
        """Show detailed information about a specific algorithm."""
        algo_type = ExerciseManager.get_by_command(command)
        if not algo_type:
            console.print(f"[red]Algorithme '{command}' non trouvé[/red]")
            return

        info = ExerciseManager.get_algorithm_info(algo_type)
        is_implemented = ExerciseManager.is_algorithm_available(algo_type)

        # Create detailed info panel
        details = []
        details.append(f"[yellow]Catégorie:[/yellow] {info.category}")
        details.append(f"[yellow]Commande:[/yellow] {info.command}")
        details.append(f"[yellow]Description:[/yellow] {info.description}")
        details.append(f"[yellow]Exercice:[/yellow] {info.exercise}")

        # Add parameter information
        if info.parameters:
            params_str = ", ".join(info.parameters)
            details.append(f"[yellow]Paramètres:[/yellow] {params_str}")

        status_text = "[green]✓ Implémenté[/green]" if is_implemented else "[red]✗ Non implémenté[/red]"
        details.append(f"[yellow]État:[/yellow] {status_text}")

        panel_content = "\n".join(details)

        console.print(Panel(
            panel_content,
            title=f"[bold]{info.name}[/bold]",
            border_style="green" if is_implemented else "red",
        ))

    def run_interactive_mode(self) -> str | None:
        """Run the interactive menu mode."""
        logger.debug("Starting interactive menu mode")

        console.print()

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            match choice:
                case "quit":
                    console.print("\n[bold green]Au revoir! 👋[/bold green]")
                    return None

                case "help":
                    self.show_help()
                    continue

                case "list":
                    self.list_algorithms_by_category()
                    continue

                case _:
                    # Show algorithm details and confirm
                    self.show_algorithm_details(choice)

                    confirm = Prompt.ask(
                        "\n[bold]Lancer cet exercice?[/bold]",
                        choices=["y", "n", "back"],
                        default="y",
                    )

                    if confirm == "y":
                        return choice
                    if confirm == "back":
                        continue
                    console.print("\n[dim]Retour au menu...[/dim]\n")

def display_welcome() -> None:
    """Display welcome message and application info."""
    # Count implemented vs total algorithms
    total_algos = len(ExerciseManager.get_all_algorithms())
    implemented_algos = sum(
        1 for algo in ExerciseManager.get_all_algorithms()
        if ExerciseManager.is_algorithm_available(algo)
    )

    welcome_text = (
        f"[bold blue]🧮 TP Algorithme Semestre 2[/bold blue]\n"
        f"\n[bold green]Simon BIDET - Rémi Renault[/bold green]\n\n"
        f"[dim]Algorithmes de graphes et structures de données[/dim]\n\n"
        f"[green]{implemented_algos}/{total_algos} algorithmes implémentés[/green]"
    )

    console.print(Panel.fit(welcome_text, border_style="blue"))
