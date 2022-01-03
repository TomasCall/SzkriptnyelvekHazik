
def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    """
    A függvény visszaadja, hogy a text mely karaktereket tartalmazza a chars-ból.
    A text egy kötelező paraméter ez a bemeneti string amit vizsgálunk
    A chars a karakterek amiket vizsgálunk, hogy benne vannak-e a stringben.
    """
    return "".join([character for character in text if character in chars])


def main():
    print(f"text = Barking! chars = ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 result = {valid('Barking')}")
    print(f"text = KL754 chars = 0123456789 result = {valid('KL754', '0123456789')}")
    print(f"text = BEAN chars = abcdefghijklmnopqrstuvwxyz result = {valid('BEAN', 'abcdefghijklmnopqrstuvwxyz')}")


if __name__=="__main__":
    main()