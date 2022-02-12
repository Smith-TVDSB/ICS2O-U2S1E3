import pytest
import student 



def test_BA():
    input_values=['Bruce','Alfred']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "false" in output[2].lower()

def test_bA():
    input_values=['bruce','Alfred']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "false" in output[2].lower()

def test_Ba():
    input_values=['Bruce','alfred']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "false" in output[2].lower()

def test_AB():
    input_values=['Alfred','Bruce']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "true" in output[2].lower()

def test_aB():
    input_values=['alfred','Bruce']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "true" in output[2].lower()

def test_Ab():
    input_values=['Alfred','bruce']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "true" in output[2].lower()


def test_BB():
    input_values=['Bruce','Bruce']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "true" in output[2].lower()

def test_more():
    input_values=['Brute','Bruce']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "false" in output[2].lower()