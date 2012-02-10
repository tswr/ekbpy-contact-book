# -*- coding: utf-8 -*-

def CSVParse(fileHandle):
    """
    Разбирает csv файл по переданному открытому хендлу.
    Возвращает список словарей. Ключи в словарях - заголовки csv файла, значения - соответствующие заголовкам данные.
    """
    lines = fileHandle.readlines()
    lines = map(lambda x: x.strip(), lines)

    headers = lines[0].split(',')
    
    out = []	
    for i in xrange(1, len(lines)):
        row = lines[i].split(',')
        out_dict = {}
        for j in xrange(0, min(len(row), len(headers))):
            out_dict[headers[j]] = row[j]
        out.append(out_dict)                        
   
    return out
	
    #raise NotImplementedError

##############
# unit tests #
##############

import unittest
import StringIO

class CSVParserTestCase(unittest.TestCase):

    def test_simple(self):
        test = "one,two,three\n1,2,3\n4,5,6"
        expectedRes = [{"one":"1","two":"2","three":"3"},{"one":"4","two":"5","three":"6"}]
        sio = StringIO.StringIO(test)
        res = CSVParse(sio)
        sio.close()
        self.assertEqual(res, expectedRes)

    def test_corrupt(self):
        test = "one,two,three\n1,2\n3,4,5,6"
        expectedRes = [{"one":"1","two":"2"},{"one":"3","two":"4","three":"5"}]
        sio = StringIO.StringIO(test)
        res = CSVParse(sio)
        sio.close()
        self.assertEqual(res, expectedRes)

if __name__ == "__main__":
    unittest.main()
