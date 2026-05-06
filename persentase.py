import random
import time

def random_similarity():
    return random.uniform( 0,100) 

if __name__ == "__main__":
    nama1 = input("Masukkan nama pertama: ")
    nama2 = input("Masukkan nama kedua: ")

    similarity_percent = random_similarity()
    print(f"Tingkat kecocokan: {similarity_percent:.2f}%")

    time.sleep(10)