# ======================== Information ========================
# Direct Link: https://www.hackerrank.com/contests/ujian-praktikum-ap-sesi-2-gojo/challenges/data-covid
# Difficulty: Medium

# ======================== Solusi ========================

array_1 = input().split()
array_2 = input().split()

def Mencari_F1_Score(array_1, array_2):
    # Confusion matrix
    True_Positive = 0
    True_Negative = 0
    False_Positive = 0
    False_Negative = 0

    for asli, prediksi in zip(array_1, array_2):
            if asli == 'Positif' and prediksi == 'Positif':
                True_Positive += 1
            elif asli == 'Positif' and prediksi == 'Negatif':
                False_Positive += 1

            elif asli == 'Negatif' and prediksi == 'Negatif':
                True_Negative += 1
            elif asli == 'Negatif' and prediksi == 'Positif':
                False_Negative += 1

    # Kalkulasi precision dan recall
    precision = True_Positive / (True_Positive + False_Positive)
    recall = True_Positive / (True_Positive + False_Negative)

    # Hasil
    return 2 * (precision * recall / precision + recall)

F1_Score = Mencari_F1_Score(array_1, array_2)
print(f'{F1_Score:.2f}')


# ======================== Test Case ========================
''' Test Case 0 '''
array_1 = ['Positif', 'Positif', 'Positif', 'Negatif', 'Negatif', 'Positif', 'Negatif', 'Positif', 'Negatif']
array_2 = ['Negatif', 'Positif', 'Negatif', 'Positif', 'Positif', 'Positif', 'Positif', 'Positif', 'Negatif']
F1_Score = Mencari_F1_Score(array_1, array_2)
print(f'{F1_Score:.2f}')

''' Test Case 1 '''
array_1 = ['Negatif', 'Negatif', 'Positif', 'Positif', 'Positif']
array_2 = ['Negatif', 'Positif', 'Positif', 'Negatif', 'Positif']
F1_Score = Mencari_F1_Score(array_1, array_2)
print(f'{F1_Score:.2f}')

''' Test Case 2 '''
array_1 = ['Negatif', 'Positif', 'Positif', 'Positif', 'Positif', 'Negatif', 'Positif', 'Negatif']
array_2 = ['Negatif', 'Positif', 'Negatif', 'Positif', 'Negatif', 'Positif', 'Positif', 'Positif']
F1_Score = Mencari_F1_Score(array_1, array_2)
print(f'{F1_Score:.2f}')

''' Test Case 3 '''
array_1 = ['Negatif', 'Positif', 'Positif', 'Positif', 'Negatif']
array_2 = ['Positif', 'Negatif', 'Positif', 'Negatif', 'Positif']
F1_Score = Mencari_F1_Score(array_1, array_2)
print(f'{F1_Score:.2f}')