# -*- coding: utf-8 -*- 
import sys, os, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from django.test import SimpleTestCase
from model.dao import dao
        
class TestDAO(SimpleTestCase):

    def setUp(self):    #configura ambiente para teste

        #descobre qual metodo será chamado e formata a saída
        func = str(self.id).split('=')[-1][:-2]
        func = func.split('test_')[-1]
        func = func.replace('_',' ')
        out = '\rTeste de ' + func + ' '
        print out.ljust(65,'-'),

    def tearDown(self):
        # informa que o teste foi realizado
        print 'Done'                                

    
    def test_existing_DAO_instance(self):
        testDAO = dao.DAO('ocorrencia')
        self.assertIsNotNone(testDAO)
    
    def test_existing_possiblesDAOS_instance(self):
        testDAO = dao.DAO('ocorrencia')
        for keyDAO in testDAO.keys:
            possibleDAO = dao.DAO(keyDAO)
            self.assertIsNotNone(possibleDAO)
            
    def test_consulta_todos(self):
        testDAO = dao.DAO('ocorrencia')
        for keyDAO in testDAO.keys:
            possibleDAO = dao.DAO(keyDAO)
            self.assertIsNotNone(possibleDAO.consulta_todos(2))
            
    def test_troca_tabela(self):
        testDAO = dao.DAO('ocorrencia')
        for keyDAO in testDAO.keys:
            possibleDAO = dao.DAO(keyDAO)
            actualPossibleDAO = possibleDAO 
            changingPossibleDAO = possibleDAO.troca_tabela('causaacidente')
            self.assertIsNotNone(changingPossibleDAO)
            self.assertNotEquals(changingPossibleDAO, actualPossibleDAO)
     