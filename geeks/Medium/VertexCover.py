# 이건 모든 u,v 사이의 edge에서 u,v 중 하나는 S에 속해야되는 문제
def vcp(visited, node):
    if node is None:
        return 0
    if visited:
        return 1 + vcp(False, node.left) + vcp(False, node.right)
    else:
        return vcp(True, node.left) + vcp(True, node.right)

def vCover(root, st):

    if (root == None):
        return 0

    if (root.left == None and root.right == None):
        return 0

    size_incl = (1 + vCover(root.left, st + 1) + vCover(root.right, st + 1))
    size_excl = 0
    if (root.left):
        size_excl += (1 + vCover(root.left.left, st + 1) + vCover(root.left.right, st + 1))
    if (root.right):
        size_excl += (1 + vCover(root.right.left, st + 1) + vCover(root.right.right, st + 1))
    return min(size_incl, size_excl)


def main():
    root = []
    print(min(vcp(True, root), vcp(False, root)))

if __name__ == '__main__':
    main()