import pytest

from stringUtils import StringUtils
string_utils = StringUtils()

#@pytest.mark.parametrize('input_text, output_text',[
#   ("кукла", "Кукла"), ("WOMEN", "woman"), ("123", "123"),
#   ]
#)
#def test_capitilize_positive(input_text, output_text):
  #  stringUtils = StringUtils()
  #  assert stringUtils.capitalize(input_text) == output_text

#@pytest.mark.parametrize('input_text, output_text',[
#   ("000", "000"), ("", "")
 #  ]
#)
#def test_capitilize_negative(input_text, output_text):
    #stringUtils = StringUtils()
    #assert stringUtils.capitalize(input_text) == output_text

def test_capitilize_positive():
    assert string_utils.capitilize("кукла") == "Кукла"
    assert string_utils.capitilize("WOMAN") == "Woman"
    assert string_utils.capitilize("123") == "123"
def test_capitilize_negative():
    assert string_utils.capitilize("") == ""
    assert string_utils.capitilize(" ") == " "
    assert string_utils.capitilize("000") == "000"

def test_trim_positive():
    assert string_utils.trim(" 123") == "123"
    assert string_utils.trim(" city ") == "city "
    assert string_utils.trim("key ") == "key "
def test_trim_negative():
    assert string_utils.trim("") == ""
    assert string_utils.trim(" ") == ""
    assert string_utils.trim("000") == "000"

def test_to_list_positive():
    assert string_utils.to_list("f,p,l,k") == ["f", "p", "l", "k"]
    assert string_utils.to_list("9:8:7:6") == ['9:8:7:6']
    assert string_utils.to_list("hh:pp:uu:ll") == ['hh:pp:uu:ll']
def test_to_list_negative():
    assert string_utils.to_list("") == []
    assert string_utils.to_list(" ") == []
    assert string_utils.to_list("000") == ["000"]

def test_contains_positive():
    assert string_utils.contains("Flat", "F") == True
    assert string_utils.contains("Home", "F") == False
    assert string_utils.contains("Appartmance", "A") == True
@pytest.mark.xfail
def test_contains_negative():
    assert string_utils.contains("") == ""
    assert string_utils.contains(" ") == " "
    assert string_utils.contains("000") == "000"

def delete_symbol_positive():
    assert string_utils.delete_symbol("Girl", "i") == "Grl"
    assert string_utils.delete_symbol("Women", "men") == "Wo"
    assert string_utils.delete_symbol("Men", "e") == "Mn"
def delete_symbol_negative():
    assert string_utils.delete_symbol("") == ""
    assert string_utils.delete_symbol(" ") == " "
    assert string_utils.delete_symbol("000") == "000"

def starts_with_positive():
    assert string_utils.starts_with("Girl", "G") == True
    assert string_utils.starts_with("Women", "W") == True
    assert string_utils.starts_with("Men", "E") == False
def starts_with_negative():
    assert string_utils.starts_with("") == ""
    assert string_utils.starts_with(" ") == " "
    assert string_utils.starts_with("000") == "000"

def end_with_positive():
    assert string_utils.end_with("Girl", "l") == True
    assert string_utils.end_with("Women", "n") == True
    assert string_utils.end_with("Men", "e") == False
def end_with_negative():
    assert string_utils.end_with("") == ""
    assert string_utils.end_with(" ") == " "
    assert string_utils.end_with("000") == "000"

def is_empty_positive():
    assert string_utils.is_empty("House") == False
    assert string_utils.is_empty("Home") == False
    assert string_utils.is_empty("") == True
def is_empty_negative():
    assert string_utils.is_empty("") == ""
    assert string_utils.is_empty(" ") == " "
    assert string_utils.is_empty("000") == "000"

def list_to_string_positive():
    assert string_utils.list_to_string([1,2,9,0]) == "1, 2, 9, 0"
    assert string_utils.list_to_string(["Anna", "Maria"]) == "Anna, Maria"
    assert string_utils.list_to_string(["Anna", "Maria"], "-") == "Anna-Maria"
def list_to_string_negative():
    assert string_utils.list_to_string("") == ""
    assert string_utils.list_to_string(" ") == " "
    assert string_utils.list_to_string("000") == "000"
