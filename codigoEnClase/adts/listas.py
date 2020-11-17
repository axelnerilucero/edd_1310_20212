class Nodo:
    def __init__( self , value , siguiente = None):
        self.data = value #No estan encapsuladas
        self.siguiente = siguiente

class Linkedlist:
    def __init__( self ): #
        self.__head = None

    def is_empty( self ):
         return self.__head == None

    def append( self , value ):
        nuevo = Nodo( value )
        if self.__head == None: #self.is_empty
            self.__head = nuevo
        else:
            curr_node = self.__head
            while curr_node.siguiente != None: #Verifica que esta en el nodo final
                curr_node = curr_node.siguiente
            curr_node.siguiente = nuevo

    def transversal( self ): #Este es para recorrerlo
        curr_node = self.__head
        while curr_node != None:
            print(f"{curr_node.data} -> ", end="")
            curr_node = curr_node.siguiente
        print("")

    def remove( self , value ):
        curr_node = self.__head
        while curr_node.data != value and curr_node.siguiente !=
