def determine_progress3(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    
    if hits_spins_ratio == 0:
        return "Get going!"
    elif hits_spins_ratio >= 0.5 and hits < spins:
        return "You win!"
    elif hits_spins_ratio >= 0.25:
        return "Almost there!"
    elif hits_spins_ratio > 0:
        return "On your way!"
    else:
        return "Get going!"  # This case should never occur, but it's here for completeness

# Test function (same as before)
def test_determine_progress(determine_progress):
    # Test "Get going!" cases
    assert determine_progress(0, 0) == "Get going!"
    assert determine_progress(0, 10) == "Get going!"
    
    # Test "On your way!" cases
    assert determine_progress(1, 10) == "On your way!"
    assert determine_progress(2, 20) == "On your way!"
    
    # Test "Almost there!" cases
    assert determine_progress(3, 10) == "Almost there!"
    assert determine_progress(5, 20) == "Almost there!"
    
    # Test "You win!" cases
    assert determine_progress(5, 10) == "You win!"
    assert determine_progress(9, 10) == "You win!"
    
    # Edge cases
    assert determine_progress(10, 10) == "Almost there!"
    assert determine_progress(11, 10) == "Almost there!"
    
    print("All tests passed!")

# Run the tests
test_determine_progress(determine_progress3)