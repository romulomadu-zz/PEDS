import numpy as np # Only used to validate the result
from random import randint

def zeros(m_rows,n_columns):
	'''
	Create m by n list matrix of zeros.
	'''
	return [[0 for j in range(n_columns)] for i in range(m_rows)]

def randmat(m_rows,n_columns):
	'''
	Create m by n list matrix of random numbers between 0 and 9
	'''
	return [[randint(0, 9) for j in range(n_columns)] for i in range(m_rows)]

def naivemul(A,B):
	'''
	Multiply two list matrix using naive method.
	'''
    
    # Get matrix dimensions
	m_rowsA = len(A)
	m_rowsB = len(B)
	n_columnsA = len(A[0])
	n_columnsB = len(B[0])
    
    # Check multiplication requirement
	if n_columnsA != m_rowsB:
		raise ValueError('Incompatible dimensions.')
	else:
        
        # Create output matrix filled with zeros
		C = zeros(m_rowsA, n_columnsB)
        
        # Fill output matrix with multiplication results
		for i in range(m_rowsA):
			for j in range(n_columnsB):
				for k in range(n_columnsA):
					C[i][j] += A[i][k]*B[k][j]
	return C

def main():
    A = randmat(2,3)
    B = randmat(3,1)
    
    print("\n### Programa multiplicador de matrizes ###\n")
    
    print("Criando matrizes:\n")
    print(f"A = {A}")    
    print(f"B = {B}")
    
    print("\nCálculo da multiplicação utilizando o algoritmo implementado:\n")
    print(f"C = {naivemul(A,B)}")
          
    print("\nCálculo da multiplicação utilizando a biblioteca numpy:\n")
    print(f"C = {np.array(A).dot(np.array(B)).tolist()}")
    
if __name__ == '__main__':
    main()
          
    



