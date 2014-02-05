import unittest 

import copy




def oneRow(zb, elem):
	res = []
	for i in range(0, len(zb)):
		res.append( switch(zb, i, elem) )
	return res

def switch(zb, i, elem):
	res = copy.deepcopy(zb)
	tmp = res[i]
	tmp.append(elem)
	del res[i]
	res.append(tmp)
	return res
	
def aqq(lista):
  return lista
  
  
class Testuje(unittest.TestCase):
  
    def testSwitch1(self):
        l = [ ['a'] ]
        r = switch(l, 0, 'b')
        self.assertEquals([['a','b']], r)

    def testOneRow(self):
        res = oneRow([ [1], [2]], 3)
        print res

    def testOneRowMore(self):
        res = oneRow([ [1, 2]], 3)
        print res

    def testAqq1(self):
        l = [1]
        expected = [
                [[1]]
            ]
        out = aqq(l)
        for exp in expected:
            self.assertIn(exp, out)

    def testAqq2(self):
        l = [1, 2]
        expected = [ 
                [[1,2]],
                [[1], [2]]
            ]             
        out = aqq(l)
        for exp in expected:
            self.assertIn(exp, out)

    def testAqq3(self):
        l = [1, 2, 3]
        expected = [ 
                [[1,2,3]],
                [[1], [2], [3] ],
                [[1], [2, 3] ],
                [[1, 2], [3] ],
                [[1, 3], [2] ],
            ]             
        out = aqq(l)
        for exp in expected:
            self.assertIn(exp, out)

if __name__ == '__main__':
    unittest.main()
