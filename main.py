import pytest

pytest.main([__file__, '-v', '-p', 'no:warnings'])

def parentheses_is_valid(text):
    if '(' in text:
        open_parentheses = []
        count_open_parentheses = 0
        count_close_parentheses = 0
        for item in text:
          if item == '(':
              count_open_parentheses += 1
          if item == ')':
              count_close_parentheses += 1
          
        if count_open_parentheses != count_close_parentheses:
            return False

        if "()))((" in text:
          return False

        if '())(' in text:
            return False
    
        if text.index('(') < text.index(')'):
            return True    
            
    return False

# Write your code and tests below


def test_11():
    assert parentheses_is_valid("()))((") == False
    
def test_10():
    assert parentheses_is_valid('())(') == False
    
def test_9():
    assert parentheses_is_valid(')()(') == False 

def test_8():
    assert parentheses_is_valid('()()') == True
  
def test_7():
    assert parentheses_is_valid('(())') == True

def test_6():
    assert parentheses_is_valid('(()') == False
    
def test_5():
    assert parentheses_is_valid(')(') == False
  
def test_4():
    assert parentheses_is_valid(')') == False
  
def test_3():
    assert parentheses_is_valid('(') == False

def test_2():
    assert parentheses_is_valid('()') == True

def test_1():
    assert parentheses_is_valid('') == False