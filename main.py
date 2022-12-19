def getSkyline(buildings):
  # Caso base: se não houver edifícios, retorna uma lista vazia
  if not buildings:
    return []

  # Se houver apenas um edifício, retorna a lista de pontos do skyline desse edifício
  if len(buildings) == 1:
    return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]

  # Divide os edifícios em duas metades
  mid = len(buildings) // 2
  left_buildings = buildings[:mid]
  right_buildings = buildings[mid:]

  # Resolve cada metade de forma recursiva
  left_skyline = getSkyline(left_buildings)
  right_skyline = getSkyline(right_buildings)

  # Combina as soluções das metades para obter a solução final
  return mergeSkylines(left_skyline, right_skyline)

def mergeSkylines(left, right):
  # Índices para percorrer os skylines da esquerda e da direita
  i = 0
  j = 0

  # Lista para armazenar o resultado
  result = []

  # Enquanto houver pontos nos skylines da esquerda e da direita
  while i < len(left) and j < len(right):
    # Se o ponto da esquerda é mais à esquerda que o ponto da direita
    if left[i][0] < right[j][0]:
      # Adiciona o ponto da esquerda na lista de resultado
      result.append(left[i])
      i += 1
    # Se o ponto da direita é mais à esquerda que o ponto da esquerda
    elif right[j][0] < left[i][0]:
      # Adiciona o ponto da direita na lista de resultado
      result.append(right[j])
      j += 1
    # Se os pontos são iguais
    else:
      # Adiciona o ponto mais alto na lista de resultado
      result.append([left[i][0], max(left[i][1], right[j][1])])
      i += 1
      j += 1

  # Adiciona os pontos restantes dos skylines da esquerda e da direita
  result.extend(left[i:])
  result.extend(right[j:])

  return result



# Exemplo de uso
buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(getSkyline(buildings))
