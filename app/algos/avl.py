from app.utils.interactivity.display.tree_print import display_avl_tree
from rich.console import Console
from rich.panel import Panel
from rich.table import Table


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance_factor(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def rotate_right(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    update_height(z)
    update_height(y)
    return y

def rotate_left(z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    update_height(z)
    update_height(y)
    return y

def insert_node(node, key):
    if not node:
        return AVLNode(key)
    if key < node.key:
        node.left = insert_node(node.left, key)
    else:
        node.right = insert_node(node.right, key)

    update_height(node)
    balance = get_balance_factor(node)

    if balance > 1 and key < node.left.key:
        return rotate_right(node)
    if balance < -1 and key > node.right.key:
        return rotate_left(node)
    if balance > 1 and key > node.left.key:
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if balance < -1 and key < node.right.key:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete_node(node, key):
    if not node:
        return node
    if key < node.key:
        node.left = delete_node(node.left, key)
    elif key > node.key:
        node.right = delete_node(node.right, key)
    else:
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        temp = min_value_node(node.right)
        node.key = temp.key
        node.right = delete_node(node.right, temp.key)

    update_height(node)
    balance = get_balance_factor(node)

    if balance > 1 and get_balance_factor(node.left) >= 0:
        return rotate_right(node)
    if balance > 1 and get_balance_factor(node.left) < 0:
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if balance < -1 and get_balance_factor(node.right) <= 0:
        return rotate_left(node)
    if balance < -1 and get_balance_factor(node.right) > 0:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def inorder_traversal(node, result=None):
    if result is None:
        result = []
    if node:
        inorder_traversal(node.left, result)
        result.append(node.key)
        inorder_traversal(node.right, result)
    return result

def json_to_avl_node(json_data):
    """Convert JSON tree data to AVL node structure with proper height calculation"""
    if not json_data:
        return None

    node = AVLNode(json_data["key"])

    # Handle left child (array format)
    left_data = json_data.get("left", [])
    if left_data:
        node.left = json_to_avl_node(left_data[0])

    # Handle right child (array format)
    right_data = json_data.get("right", [])
    if right_data:
        node.right = json_to_avl_node(right_data[0])

    # IMPORTANT: Recalculer la hauteur après avoir créé les enfants
    update_height(node)

    return node

def rebuild_balanced_tree(root):
    """Reconstruit un arbre AVL équilibré à partir d'un arbre existant"""
    if not root:
        return None

    # Parcours in-order pour récupérer les valeurs triées
    values = inorder_traversal(root)

    # Reconstruire l'arbre de manière équilibrée
    def build_balanced(sorted_values):
        if not sorted_values:
            return None

        mid = len(sorted_values) // 2
        node = AVLNode(sorted_values[mid])

        node.left = build_balanced(sorted_values[:mid])
        node.right = build_balanced(sorted_values[mid + 1:])

        update_height(node)
        return node

    return build_balanced(values)

def is_well_balanced(node):
    """Check if tree is well balanced (stricter than AVL requirements)"""
    if not node:
        return True

    balance = get_balance_factor(node)
    # Be more strict: prefer balance factor of 0 when possible
    if abs(balance) > 1:
        return False

    # Check if the tree structure could be improved
    left_height = get_height(node.left)
    right_height = get_height(node.right)

    # If there's a significant height difference, it's not well balanced
    return (abs(left_height - right_height) <= 1 and
            is_well_balanced(node.left) and
            is_well_balanced(node.right))

# ======================================
# FONCTIONS PRINCIPALES POUR L'INTERFACE
# ======================================

def insert(tree_data, number_list):
    """Fonction principale pour l'insertion dans l'arbre AVL"""
    root = json_to_avl_node(tree_data) if tree_data else None

    # Afficher l'arbre initial s'il existe
    if root:
        display_avl_tree(root, "Arbre initial depuis JSON")

        # TOUJOURS rééquilibrer l'arbre initial (il vient du JSON)
        root = rebuild_balanced_tree(root)
        display_avl_tree(root, "Arbre initial rééquilibré")

    # Insérer chaque élément ET forcer un rééquilibrage complet après chaque insertion
    for number in number_list:
        if root is None:
            root = insert_node(None, number)
        else:
            root = insert_node(root, number)
            # Force un rééquilibrage complet après chaque insertion
            root = rebuild_balanced_tree(root)

    if root:
        display_avl_tree(root, "Arbre après insertions")
        return root
    return None

def delete(tree_data, number_list):
    """Fonction principale pour la suppression dans l'arbre AVL"""
    console = Console()
    root = json_to_avl_node(tree_data) if tree_data else None

    if not root:
        # Créer l'arbre avec rééquilibrage
        for number in number_list:
            root = insert_node(root, number)
        root = rebuild_balanced_tree(root)
    else:
        # TOUJOURS rééquilibrer l'arbre initial
        root = rebuild_balanced_tree(root)

    display_avl_tree(root, "Arbre initial")

    # Supprimer tous les éléments de la liste
    if number_list and root:
        initial_values = inorder_traversal(root)
        
        # Panel d'information sur la suppression
        console.print(Panel.fit(
            f"[bold yellow]🗑️ Suppression d'éléments[/bold yellow]",
            border_style="yellow",
        ))
        
        # Table des éléments
        info_table = Table(show_header=True, header_style="bold magenta")
        info_table.add_column("Type", style="cyan", no_wrap=True)
        info_table.add_column("Éléments", style="yellow")
        
        info_table.add_row("À supprimer", str(number_list))
        info_table.add_row("Présents dans l'arbre", str(initial_values))
        
        console.print(info_table)

        for to_delete in number_list:
            if root:  # Vérifier que l'arbre n'est pas vide
                current_values = inorder_traversal(root)
                
                console.print(f"\n[bold blue]🔍 Tentative de suppression de {to_delete}[/bold blue]")
                console.print(f"[dim]Valeurs actuelles: {current_values}[/dim]")

                if to_delete in current_values:
                    console.print(f"[green]✓ {to_delete} trouvé, suppression en cours...[/green]")
                    root = delete_node(root, to_delete)

                    # Rééquilibrage après suppression
                    if root:
                        root = rebuild_balanced_tree(root)
                        new_values = inorder_traversal(root)
                        console.print(f"[green]✓ Suppression réussie. Nouvelles valeurs: {new_values}[/green]")
                        display_avl_tree(root, f"Arbre après suppression de {to_delete}")
                    else:
                        console.print(f"[green]✓ Arbre vide après suppression de {to_delete}[/green]")
                        display_avl_tree(root, f"Arbre vide après suppression de {to_delete}")
                        break
                else:
                    console.print(f"[red]✗ {to_delete} non trouvé dans l'arbre[/red]")
            else:
                console.print(f"[red]Arbre déjà vide, impossible de supprimer {to_delete}[/red]")
                break

        return root

    return root

def get_balance(tree_data):
    """Fonction principale pour analyser l'équilibrage"""
    root = json_to_avl_node(tree_data) if tree_data else None

    display_avl_tree(root, "Arbre actuel (depuis JSON)")

    # TOUJOURS proposer un rééquilibrage complet
    balanced_root = rebuild_balanced_tree(root)
    if balanced_root:
        display_avl_tree(balanced_root, "Arbre après rééquilibrage complet")

    return f"Analyse terminée - Arbre original: {inorder_traversal(root)}"
