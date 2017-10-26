class Trees:
    def __init__(self,val):
        self.right = None
        self.left  = None
        self.value = None

    def ipostorder(self, root):
        if root:

            self.inorder(root.left)
            self.inorder(root.right)
            print root.value


t = Trees(3)
a = Trees(4)
b = Trees(5)
t.right = a
t.left = b
a.inorder(t)
