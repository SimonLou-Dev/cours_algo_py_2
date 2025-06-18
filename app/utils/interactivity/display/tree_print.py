"""Interactive utilities for algorithm visualization and user interaction."""

from typing import Any, Optional

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.tree import Tree


def display_avl_tree(root_node: Any, title: str = "Arbre AVL", console: Optional[Console] = None) -> None:
    """Display an AVL tree with beautiful formatting using Rich.
    
    Args:
        root_node: The root node of the AVL tree (should have .key, .left, .right, .height attributes)
        title: Title for the display panel
        console: Rich console instance (creates new one if None)

    """
    if console is None:
        console = Console()

    # Add line break before displaying
    console.print()

    # Main title panel
    console.print(Panel.fit(
        f"[bold cyan]🌳 {title} 🌳[/bold cyan]",
        border_style="cyan",
    ))

    if not root_node:
        console.print("[red]Arbre vide[/red]")
        return

    # Helper functions for tree analysis
    def get_height(node):
        """Get height of a node (works with AVL nodes)."""
        if not node:
            return 0
        return getattr(node, "height", 1)

    def get_balance_factor(node):
        """Get balance factor of a node."""
        if not node:
            return 0
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        return left_height - right_height

    def inorder_traversal(node, result=None):
        """Perform inorder traversal."""
        if result is None:
            result = []
        if node:
            inorder_traversal(node.left, result)
            result.append(node.key)
            inorder_traversal(node.right, result)
        return result

    def get_tree_stats(node):
        """Get tree statistics (node count, height)."""
        if not node:
            return 0, 0

        left_count, left_height = get_tree_stats(node.left)
        right_count, right_height = get_tree_stats(node.right)

        return (left_count + right_count + 1,
                max(left_height, right_height) + 1)

    # Calculate statistics
    node_count, tree_height = get_tree_stats(root_node)
    traversal_result = inorder_traversal(root_node)

    # Statistics table
    stats_table = Table(title="📊 Statistiques", show_header=True, header_style="bold magenta")
    stats_table.add_column("Propriété", style="cyan", no_wrap=True)
    stats_table.add_column("Valeur", style="yellow")

    stats_table.add_row("Nombre de nœuds", str(node_count))
    stats_table.add_row("Hauteur", str(tree_height))
    stats_table.add_row("Parcours in-order", str(traversal_result))

    console.print(stats_table)
    console.print()

    # Tree structure visualization
    console.print("[bold blue]🌲 Structure de l'arbre:[/bold blue]")

    def build_rich_tree(node, rich_node=None):
        """Build Rich tree visualization recursively."""
        if not node:
            return None

        # Get node properties
        balance = get_balance_factor(node)
        height = get_height(node)

        # Modification : considérer |balance| <= 1 comme équilibré
        if abs(balance) <= 1:
            emoji = "🟢"
            color = "green"
        else:
            emoji = "🔴"
            color = "red"

        # Create node label
        label = f"{emoji} [{color}]{node.key}[/{color}] [dim](h:{height}, b:{balance:+d})[/dim]"

        if rich_node is None:
            # Root node
            tree = Tree(label)
            current_rich_node = tree
        else:
            # Child node
            current_rich_node = rich_node.add(label)

        # Add children
        if node.left or node.right:
            if node.left:
                build_rich_tree(node.left, current_rich_node)
            else:
                current_rich_node.add("[dim]∅[/dim]")

            if node.right:
                build_rich_tree(node.right, current_rich_node)
            else:
                current_rich_node.add("[dim]∅[/dim]")

        return tree if rich_node is None else current_rich_node

    # Build and display tree
    tree = build_rich_tree(root_node)
    console.print(tree)

    # Modification : légende mise à jour
    console.print()
    console.print("[dim]🟢 Équilibré (|b|≤1)  🔴 Déséquilibré (|b|>1)  ∅ Nœud vide[/dim]")


def display_algorithm_result(algorithm_name: str, result: Any, execution_time: float = 0.0, console: Optional[Console] = None) -> None:
    """Display algorithm execution result with formatting.
    
    Args:
        algorithm_name: Name of the executed algorithm
        result: Result of the algorithm execution
        execution_time: Time taken for execution in seconds
        console: Rich console instance (creates new one if None)

    """
    if console is None:
        console = Console()

    # Result panel
    console.print(Panel.fit(
        f"[bold green]✅ Résultat: {algorithm_name}[/bold green]",
        border_style="green",
    ))

    # Display result based on type
    if isinstance(result, (list, tuple)):
        console.print(f"[cyan]Résultat:[/cyan] {result}")
    elif isinstance(result, dict):
        result_table = Table(title="Résultat", show_header=True)
        result_table.add_column("Clé", style="cyan")
        result_table.add_column("Valeur", style="yellow")
        for key, value in result.items():
            result_table.add_row(str(key), str(value))
        console.print(result_table)
    else:
        console.print(f"[cyan]Résultat:[/cyan] {result}")

    # Execution time if provided
    if execution_time > 0:
        console.print(f"[dim]⏱️ Temps d'exécution: {execution_time:.6f} secondes[/dim]")


def display_error(error_message: str, console: Optional[Console] = None) -> None:
    """Display error message with formatting.
    
    Args:
        error_message: Error message to display
        console: Rich console instance (creates new one if None)

    """
    if console is None:
        console = Console()

    console.print(Panel.fit(
        f"[bold red]❌ Erreur: {error_message}[/bold red]",
        border_style="red",
    ))


def display_step_by_step_demo(steps: list[tuple[str, Any]], title: str = "Démonstration étape par étape", console: Optional[Console] = None) -> None:
    """Display a step-by-step demonstration.
    
    Args:
        steps: List of (description, result) tuples
        title: Title for the demonstration
        console: Rich console instance (creates new one if None)

    """
    if console is None:
        console = Console()

    console.print(Panel.fit(
        f"[bold yellow]🔧 {title} 🔧[/bold yellow]",
        border_style="yellow",
    ))

    for i, (description, result) in enumerate(steps, 1):
        console.print(f"\n[bold cyan]📍 Étape {i}: {description}[/bold cyan]")

        if hasattr(result, "key"):  # Likely an AVL node
            display_avl_tree(result, f"Étape {i}", console)
        else:
            console.print(f"[green]Résultat:[/green] {result}")
