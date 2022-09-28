import unittest
from zookeeper import Ztree

class TestZookeeper(unittest.TestCase):

    def test_crear_znode(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        self.assertEqual(tree.getData('/node1'), 'algo')

    def test_no_se_puede_crear(self):
        with self.assertRaises(Exception):
            tree = Ztree()
            tree.create('/node1/node2/node3', 'algo', True, True, 10, None)
    
    #Caso 1 propuesto
    def test_crear_hijo_node1(self):
        tree = Ztree()
        tree.create('/node1', 'algo', True, True, 10, '/')
        tree.create('/node1/node2', 'otra_cosa', True, True, 50, '/node1')
        print('\t\tPrueba 1: Creando un nodo hijo a node1')
        tree.showTree()
        self.assertEqual(tree.getData('/node1/node2'), 'otra_cosa')
    
    #Caso 2 propuesto
    def test_eliminar_nodo_existente(self):
        tree=Ztree()
        tree.create('/node1', 'contenido1', True, True, 40, '/')
        tree.create('/node1/node2', 'contenido2', True, True, 50, '/node1')
        tree.create('/node1/node3', 'contenido3', False, False, 50, '/node1')
        print('\t\tPrueba 2: Eliminando un nodo')
        tree.showTree()
        tree.delete('/node1/node3',0)
        tree.showTree()
        self.assertEqual(tree.getData('/node1'), 'contenido1')

    #Caso 3 propuesto
    def test_eliminar_nodo_no_existente(self):
        tree=Ztree()
        tree.create('/node1', 'contenido1', True, True, 40, '/')
        tree.showTree()
        with self.assertRaises(Exception):
            print('\t\tPrueba 3: Eliminadno un nodo que no existe')
            tree.delete('/node1/node2')
        tree.showTree()

    #Caso 4 propuesto     
    def test_mostrar_nodo(self):       
        tree=Ztree()
        tree.create('/node1', 'contenido1', True, True, 40, '/')
        tree.create('/node1/node2', 'contenido2', True, True, 50, '/node1')
        tree.create('/node1/node3', 'contenido3', False, False, 50, '/node1')
        print('\t\tPrueba 4: Mostrando información del node3')
        tree.showNode('/node1/node3')
        self.assertEqual(tree.getData('/node1/node3'), 'contenido3')
  
    #Caso 5 Propuesto
    def test_cambiar_info_nodo(self):
        tree=Ztree()
        tree.create('/node1', 'contenido1', True, True, 40, '/')
        tree.create('/node1/node2', 'contenido2', True, True, 50, '/node1')
        print('\t\tPrueba 5: Cambiando la información del node2')
        tree.showNode('/node1/node2')
        tree.setData('/node1/node2','contenido4')
        tree.showNode('/node1/node2')
        self.assertEqual(tree.getData('/node1/node2'), 'contenido4')

if __name__ == '__main__':
    unittest.main()

