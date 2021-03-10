"""모듈 설명 제목 
    
    * 소스코드의 첫 시작부분에 기재할 것 
    * import보다 앞서서 기재할 것 
    
Todo: 
    TODO리스트를 기재 
        * conf.py의``sphinx.ext.todo`` 를 적용하지 않으면 사용할 수 없다. 
        * conf.py의``todo_include_todos = True``로 하지 않으면 보이지 않는다. 
        
""" 

import json 
import inspect 

class testClass() : 
    """클래스 설명 제목 
    
    클래스에 대한 설명문 
    
    Attributes: 
        속성의 이름 (속성의 데이터형): 속성의 설명 
        속성의 이름 (:obj:`속성의 데이터형`): 속성의 설명. 
    """ 
    
    
    def print_test(self, param1, param2) : 
        
        """함수 설명 제목 
            함수에 대한 설명문
             
            Args: 
                인수의 이름 (인수의 데이터형): 
                인수의 설명 인수의 이름 (:obj:`인수의 데이터형`, optional): 인수의 설명 
                

            Returns: 리턴 값의 데이터형: 
                리턴 값의 설명(예 : True 라면 성공, False이라면 실패.) 
                

            Raises: 
                예외명: 예외의 설명 (예 : 인수가 지정되지 않은 경우에 발생 ) 
            

            Yields: 
                리턴값의 데이터형: 리턴값에 대한 설명 
            

            Examples: 
                함수의 사용법 기재 >>> print_test ("test", "message") test message 
            

            Note: 
                주의항목 등을 기재
     """ 
    
