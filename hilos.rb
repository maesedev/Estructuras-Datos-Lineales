
def suma_thread(numbers)
    sum = numbers.reduce(:+)
    puts "Suma: #{numbers.join(' + ')} = #{sum}"
  end
  
  def multiplicacion_thread(numbers)
    product = numbers.reduce(:*)
    puts "Multiplicación: #{numbers.join(' * ')} = #{product}"
  end
  
  # Genera 10 números aleatorios
  random_numbers = Array.new(10) { rand(1..100) }
  
  # Crea los hilos para la suma y multiplicación
  suma_hilo = Thread.new { suma_thread(random_numbers) }
  multiplicacion_hilo = Thread.new { multiplicacion_thread(random_numbers) }
  
  # Espera a que ambos hilos terminen
  suma_hilo.join
  multiplicacion_hilo.join
  
  puts "Fin del programa."

  