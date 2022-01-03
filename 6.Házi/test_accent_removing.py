from accent_removing import accent_removal

def test_accent_removal():
    assert accent_removal("alma") == "alma"
    assert accent_removal("álmos") == "almos"
    assert accent_removal("ALMA") == "ALMA"
    assert accent_removal("") == ""
    assert accent_removal("áéíóöőúüűÁÉÍÓÖŐÚÜŰ") == "aeiooouuuAEIOOOUUU"