def sortfunc(e):
  return numbers[e[0]]+numbers[e[1]]

if __name__ == "__main__":
  with open('Day1input.text', 'r') as f:
    numbers = [int(x) for x in f.read().split()]
  # numbers = [1721, 979, 366, 299, 675, 1456]

  # Preamble
  numbers.sort()

  # Part 1
  x = 0

  for i in range(len(numbers)):
    y = len(numbers)-i-1
    if numbers[x]+numbers[y] == 2020:
      print(numbers[x],numbers[y])
      print(numbers[x]*numbers[y])
      break
    elif numbers[x]+numbers[y] < 2020:
      x += 1

  # Part 2
  x = 0
  y = len(numbers)-1
  zsum = []
  znum = []

  for x in range(len(numbers)):
      for y in range(len(numbers)):
          if numbers[x]+numbers[y] < 2020:
              zsum.append(numbers[x]+numbers[y])
              znum.append([x,y])

  znum.sort(key = sortfunc)
  zsum.sort()

  for number in numbers:
    for i in range(len(zsum)):
      if number + zsum[i] == 2020:
        print(numbers[znum[i][0]], numbers[znum[i][1]], number)
        print(numbers[znum[i][0]]*numbers[znum[i][1]] * number)
        break
      else:
        continue
    break

    # thoughts, not a nice solution but it works better than n^3 time.
    # could use sets to make this better and that'd be my next approach
