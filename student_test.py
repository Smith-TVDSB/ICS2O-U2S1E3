import pytest
import student 



def test_BA(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert "false" in out[-8:].lower()

def test_bA(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert "false" in out[-8:].lower()

def test_Ba(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert "false" in out[-8:].lower()

def test_AB(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert "true" in out[-8:].lower()

def test_aB(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert "true" in out[-8:].lower()

def test_Ab(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert "true" in out[-8:].lower()


def test_BB(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert "true" in out[-8:].lower()

def test_more(capsys):
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
    student.main()

    out, err = capsys.readouterr()
    assert "false" in out[-8:].lower()
