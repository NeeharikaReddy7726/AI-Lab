
facts = {#facts
    "Loves(John,Mary)",
    "Loves(Mary,John)",
    "Kind(John)"
}

#functions
def loves_implies_happy(x):
    return f"Happy({x})"

def happy_implies_smiles(x):
    return f"Smiles({x})"

def smiles_implies_friendly(x):
    return f"Friendly({x})"

def friendly_implies_not_sad(x):
    return f"~Sad({x})"

def sad_implies_not_happy(x):
    return f"~Happy({x})"


derived = set()

if "Kind(John)" in facts:
    facts.add("Loves(John,Everyone)")

for fact in list(facts):
    if "Loves(John" in fact:
        derived.add("Happy(John)")

derived.add("~Happy(John)")

if "Happy(John)" in derived and "~Happy(John)" in derived:
    print("Contradiction found!")
    print("Therefore, John is Happy ")
else:
    print("No conclusion")