'''
#tree 

class Tree:
    def __init__(self,size):
        self.tree = {}
        self.marked = {}
        self.size = size

        for i in range(size):
            self.tree[chr(i+65)] = []
            self.marked[chr(i+65)] = 0
    
    def link(self,src,dst):
        self.tree[src].append(dst)
    
    def DFS(self, root):
        stack = [root,]
        while stack:
            v = stack.pop()
            if not self.marked[v]:
                print(v,end=" ")
                self.marked[v] = True 
                for children in self.tree[v]:
                    if not self.marked[children]:
                        stack.append(children)
        print()

    def BFS(self,root):
        queue = [root,]
        while queue:
            v = queue[0]
            del queue[0]
            if not self.marked[v]:
                print(v,end=" ")
                self.marked[v] = True
                for children in self.tree[v]:
                    if not self.marked[children]:
                        queue.append(children)

    def display(self):
        for x,y in self.tree.items():
            print(f"{x} : {y}")

a = Tree(6)
a.link('A','B')
a.link('A','C')
a.link('A','D')
a.link('C','E')
a.link('C','F') 
a.display()

a.BFS('A')

#  Maze traversal code 

class Maze:
    def __init__(self):
        self.maze = [['#','#','#','#','#',' ','#'],
                     [' ',' ','#',' ','#',' ',' '],
                     ['#',' ','#',' ','#',' ','#'],
                     ['#',' ',' ',' ','#',' ','#'],
                     ['#',' ','#',' ',' ',' ','#'],
                     [' ',' ','#','#',' ','#','#'],
                     ['#','#','#','#',' ','#','#']]
        self.marked = set()
    
    def move(self, start_i, start_j, type='DFS'):
        no = 0
        datastruct = [[start_i, start_j], ]
        while datastruct:
            if type == 'DFS':
                m = datastruct.pop()
            else:
                m = datastruct[0]
                del datastruct[0]
            
            i, j = m[0], m[1]
            if (i, j) not in self.marked:
                self.maze[i][j] = no 
                self.marked.add((i, j)) 
                no += 1
            
                for del_i, del_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ni, nj = i + del_i, j + del_j
                    l = len(self.maze) 
                    if (0 <= ni < l and 0 <= nj < l) and (self.maze[ni][nj] == ' ') and (ni, nj) not in self.marked:
                        datastruct.append([ni, nj])

    def display(self):
        for i in range(7):
            for j in range(7):
                print(self.maze[i][j],end=" ")
            print()
            

m = Maze()
m.move(5, 0, 'DFS') 
m.display()
'''

# Matrix operations

class Matrix:
    def __init__(self,m,n):                                         # constructor 
        self.l = [[0 for _ in range(n)] for _ in range(m)] 
        self.m = m 
        self.n = n     

    def __repr__(self):                     # display (print call)
        s = ''
        for i in self.l:
            s += str(i) + '\n'
        return s
    
    def fill(self,elements = []):                   # input call
        if len(elements)==0:
            print("enter Matrix elements:")
            for i in range(self.m):
                temp = input().split()
                self.l[i] = list(map(int,temp)) 
        else:
            self.l.extend(elements)
    
    def __mul__(self,other):                                # Matrix product
        if isinstance(other,Matrix) and (self.n==other.m):
            C = Matrix(self.m,other.n)
            A = []
            for i in range(self.m):
                row = []
                for j in range(other.n):
                    s = 0
                    for k in range(self.n):
                        s += self.l[i][k] * other.l[k][j]
                    row.append(s) 
                A.append(row) 
            C.l = A
            return C 
        elif isinstance(other,int):                         # dot int product
            A = Matrix(self.m,self.n)
            A.l = [[element * other for element in row] for row in self.l]
            return A

        elif isinstance(other,float):                         # dot float product
            A = Matrix(self.m,self.n)
            A.l = [[round((element * other),3) for element in row] for row in self.l]
            return A

    def __add__(self,other):                    # A + B
        if isinstance(other,Matrix):
            C = Matrix(self.m,self.n)
            if (other.m == self.m) and (other.n == self.n):
                A = [[(self.l[i][j] + other.l[i][j]) for j in range(self.n)] for i in range(self.m)]
                C.l = A
                return C
    def __sub__(self,other):                # A - B
        if isinstance(other,Matrix):
            C = Matrix(self.m,self.n)
            if (other.m == self.m) and (other.n == self.n):
                A = [[(self.l[i][j] - other.l[i][j]) for j in range(self.n)] for i in range(self.m)]
                C.l = A 
                return C


    def __xor__(self, other):  # tensor product
        if isinstance(other, Matrix):
            p = self.m * other.m
            q = self.n * other.n
            M = Matrix(p, q)
            
            A = []
            for i in self.l:
                row = []
                for j in i:
                    scaled_Matrix = other * j 
                    row.extend(scaled_Matrix.l)
                A.extend(row)
            
            swapped_A = []
            for i in range(0,len(A),4):
                try:
                    swapped_A.extend([A[i]+A[i+2]])
                    swapped_A.extend([A[i+1]+A[i+3]])
                except IndexError:
                    swapped_A.append(A[i])  
                    swapped_A.append(A[i+1]) 
            M.l = swapped_A
            return M
        
    def t(self):                        # transpose 
        C = Matrix(self.n,self.m) 
        for i in range(self.n):
            for j in range(self.m):
                C.l[i][j] = self.l[j][i] 
        return C 

    def __eq__(self,other):     # equality 
        if self.l == other.l:
            return True 
        else:
            return False 
    
    def issym(self):                # symmetric matrices
        if self.t() == self:
            return True 
        else:
            return False
    
    def isskew(self):               # skew matrices
        if self.t() == (self * (-1)):
            return True
        else:
            return False 
        
    def express_symmetric_skew(self):                           # A = P + Q 
        P , Q = Matrix(self.m,self.n) , Matrix(self.m,self.n) 
        P = ( self + self.t() ) * 0.5
        Q = ( self - self.t() ) * 0.5
        print(P,'\n') 
        print(Q)

    def det(self):                                              # determinant
        A = self.l
        if self.m == 2:
            s = (A[0][0] * A[1][1]) - (A[0][1] * A[1][0])
            return s 
        elif self.m == 3:
            s1 = A[0][0] * ((A[1][1] * A[2][2]) - (A[1][2] * A[2][1]))
            s2 = A[0][1] * ((A[1][0] * A[2][2]) - (A[1][2] * A[2][0]))
            s3 = A[0][2] * ((A[1][0] * A[2][1]) - (A[1][1] * A[2][0]))
            return s1-s2+s3 
    
    def co_factor(self):                                    # cofactor Matrix
        if self.m == 2:
            CF = Matrix(2,2) 
            CF.l = self.l 
            CF.l[0][0],CF.l[1][1] = CF.l[1][1],CF.l[0][0] 
            CF.l[1][0],CF.l[0][1] = -CF.l[0][1],-CF.l[1][0] 
            return CF
        else:
            CF = Matrix(self.m,self.n) 
            for i in range(self.m):
                for j in range(self.n):
                    temp = Matrix(2,2)
                    t = []
                    for x in range(self.m):
                        if x != i:
                            row = []
                            for y in range(self.n):
                                if y != j:
                                    row.append(self.l[x][y])
                            t.append(row)
                    temp.l = t 
                    CF.l[i][j] = temp.det() * ((-1)**(i+j))
            return CF 
    
    def adj(self):                                          # adjacent Matrix
        return self.co_factor().t() 
        
    def inverse(self,display = 1):                  # inverse of Matrix: 1-> print , else-> val
        if display==1:
            print(f"{self.adj()} * 1/{self.det()}") 
        else:
            return self.adj() * (1/self.det())

# --------------------------- class definition ----------------------------- #

def area_of_triangle():                         # area of triangle calculation (3 2D vertices)
    A = Matrix(3,3)
    print("enter vertices:")
    for i in range(3):
        temp = input().split()
        A.l[i] = list(map(int,temp)) + [1,]  
    area = 0.5 * A.det()
    print(f"area = {area} sq units")
 

def solve_eqs():                                # X = A_inv * C     A & C i/p
    A = Matrix(3,3)
    C = Matrix(3,1)
    print('\ncoeiff Matrix:')
    A.fill()
    print("\nconstant Matrix:")
    C.fill() 

    X = (A.inverse(0) * C)
    X.l = [[round(j) for j in i] for i in X.l]
    print(X)


def main():
    size_m = input('m n:').split()                      # Matrix M
    size_m = list(map(int,size_m))

    #size_n = input('m n:').split()                      # Matrix N
    #size_n = list(map(int,size_n))
    
    
    M = Matrix(size_m[0],size_m[1])
    #N = Matrix(size_n[0],size_n[1])

    M.fill()
    #N.fill()

main() 

 
        























    