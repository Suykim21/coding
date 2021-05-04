# O(n) time | O(n) space - utilize two pointers
def sortedSquaredArray(array):
	sortedArr = [0 for _ in array] # Create new array with 0s
	smallIdx = 0 # Starting pointer
	largeIdx = len(array) - 1 # Ending pointer
	
	for i in reversed(range(len(array))): # Iterate indices backwards
		smallValue = array[smallIdx]
		largeValue = array[largeIdx]
		
		if abs(smallValue) > abs(largeValue):
			smallIdx += 1
			sortedArr[i] = smallValue ** 2
		else:
			largeIdx -= 1
			sortedArr[i] = largeValue ** 2
	
	return sortedArr

print(sortedSquaredArray([1,2,-4]))

# =====================================
# O(n) time | O(k) space - create flags to keep track of result
def tournamentWinner(competitions, results):
	currBestTeam = '' # Flag to track best team
	scores = {currBestTeam: 0}

	for idx, competition in enumerate(competitions):
		result = results[idx] # Get results
		homeTeam, awayTeam = competition # Set teams

		winningTeam = homeTeam if result == 1 else awayTeam # identify winning team

		if winningTeam not in scores: # Create new key
			scores[winningTeam] = 0

		scores[winningTeam] += 3

		if scores[winningTeam] > scores[currBestTeam]: # identify best team
			currBestTeam = winningTeam

	return winningTeam
# =====================================

# O(nlogn) time | O(1) space - where n is the number of coins
def nonConstructibleChange(coins):
	coins.sort()
	currChangeCreated = 0

	for coin in coins:
		if coin > currChangeCreated + 1:
			return currChangeCreated + 1

		currChangeCreated += coin

	return currChangeCreated + 1


