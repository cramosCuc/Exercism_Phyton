def sum_of_multiples(limite, multiplos):
    return sum(valor for valor in range(limite)
               if any(valor % multiplos == 0
                      for multiplos in multiplos
                      if multiplos > 0))
