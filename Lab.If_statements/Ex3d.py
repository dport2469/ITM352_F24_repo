def determine_progress4(hits, spins):
    if spins == 0:
        return "Get going!"
    
    hits_spins_ratio = hits / spins
    
    progress = {
        0: "Get going!",
        1: "On your way!",
        2: "Almost there!",
        3: "You win!"
    }

    progress_index =  (hits_spins_ratio > 0)*1 + (hits_spins_ratio >= 0.25)*1 + (hits_spins_ratio >= 0.5 and hits < spins)*1  # note: will be 0 if none of the conditions are met

    return progress[progress_index]

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
test_determine_progress(determine_progress4)