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
        elif not node.right:
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

# ======================================
# FONCTIONS PRINCIPALES POUR L'INTERFACE
# ======================================

def insert(tree_data, number_list):
    """Fonction principale pour l'insertion dans l'arbre AVL"""
    print("=== Insertion dans l'arbre AVL ===")
    
    root = None
    for number in number_list:
        print(f"Insertion de {number}")
        root = insert_node(root, number)
        
    # Affichage du résultat
    if root:
        result = inorder_traversal(root)
        print(f"Arbre après insertions: {result}")
        print(f"Hauteur de l'arbre: {get_height(root)}")
        return root
    else:
        print("Arbre vide")
        return None

def delete(tree_data, number_list):
    """Fonction principale pour la suppression dans l'arbre AVL"""
    print("=== Suppression dans l'arbre AVL ===")
    
    # D'abord créer un arbre avec les données
    root = None
    for number in number_list:
        root = insert_node(root, number)
    
    print(f"Arbre initial: {inorder_traversal(root)}")
    
    # Supprimer le premier élément (exemple)
    if number_list:
        to_delete = number_list[0]  # ou 30 comme dans le README
        print(f"Suppression de {to_delete}")
        root = delete_node(root, to_delete)
        
        result = inorder_traversal(root)
        print(f"Arbre après suppression: {result}")
        print(f"Hauteur de l'arbre: {get_height(root)}")
        return root
    
    return root

def get_balance(tree_data):
    """Fonction principale pour analyser l'équilibrage"""
    print("=== Analyse d'équilibrage de l'arbre AVL ===")
    
    # Créer un arbre exemple
    root = None
    test_values = [10, 20, 30, 40, 50, 25]
    
    for value in test_values:
        root = insert_node(root, value)
    
    def analyze_balance(node, depth=0):
        if not node:
            return
        
        balance = get_balance_factor(node)
        indent = "  " * depth
        print(f"{indent}Nœud {node.key}: balance={balance}, hauteur={get_height(node)}")
        
        if node.left:
            analyze_balance(node.left, depth + 1)
        if node.right:
            analyze_balance(node.right, depth + 1)
    
    analyze_balance(root)
    return f"Analyse terminée - Arbre équilibré: {inorder_traversal(root)}"