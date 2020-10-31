#Pratik Prabhakar

'''
A simple vote counting application for an election.
The application will be built on two classes named Candidate and Vote
that encapsulate the details of individual candidates in the election and 
the votes cast respectively. There will also be some code to carry
out the vote counting process and determine the winner.
'''

'''
A class Candidate encapsulate the details of each candidate (name, party, etc.)
Candidate objects support the following instance functions.
1) add_vote() : Add one to this candidate's vote tally.
2) clear_votes() : Reset this candidate's vote tally to zero.

In addition the class includes the following per-class functions.
1) lookup(name): Return the candidate with the 'name' (and None if no such candidate).
2) initialize(filename): Initialize candidates from contents of .csv file named 'fname'
which return list of all candidates.
'''
class Candidate:

    # Container for the Candidate's list of objects
    all_candidates = []
    # Container which takes key = candidate names and its votes as values
    candidate_participated = {}
    name = ''
    party = ''

    def __init__(self, name='', party=''):
        # Create a Candidate object initialized with the values provided.   
        self.__name = name
        self.__party = party
        Candidate.all_candidates.append(self)
        Candidate.candidate_participated[self.__name] = 0
        Candidate.name = self.__name
        Candidate.party = self.__party

    def lookup(name):
        # Lookup the name of the candidate in the voting list.
        if name in Candidate.candidate_participated.keys():
            return name
        else:
            return 'None'

    def add_vote(self):
        # Add count of votes to a candidate for the party.
        #cand_name = input("Please enter the name of the candidate to vote: ")
        if self in Candidate.candidate_participated:
            Candidate.candidate_participated[self]+= 1
            return Candidate.candidate_participated
        else:
            return "No candidates to vote with this name"
            
    def clear_votes():
        # Reset the count of votes to 0.
        for i in Candidate.candidate_participated:
            Candidate.candidate_participated[i] = 0
        
    def initialize(filename):
        # Read each candidate's name and party from .csv 'filename' and
        # return a list of candidates.
        try:
            afile = open(filename, "r")
            for line in afile:
                if not line.isspace():
                    col_values = [x.strip(" \n") for x in line.split(',')]
                    #print(col_values)
                    name = col_values[0]
                    Candidate.name = name
                    Candidate.party = col_values[1]
                    Candidate.candidate_participated[name]=0
            return list(Candidate.candidate_participated.keys())
        except:
            print("*** Trouble loading %s." % filename)


'''
A class Vote capture the details of an individual vote. In our system,
each vote ranks candidates in order of preference and these preferences play a role
in deciding the outcome of the election.
1) most_preferred(cands) : Return name of most preferred candidate among those in list
'cands'.

In addition the class includes the following per-class functions.
1) initialize(fname): Initialize votes from contents of .csv 
le named 'fname'. Assume
candidates appear in order of preference (highest left). Return a list of all votes.
'''
class Vote:

    cands = []
    # Container for the Vote's list of objects
    all_votes = []
    no_of_votes = 0
    
    def __init__(self, preferences):
        # Create a Vote object initialized with the values provided.   
        self.__preferences = preferences
        Vote.all_votes.append(self)
        
    def most_preferred(cands):
        # Return the list of preferred candidates.
        preferred_voting = sorted(Candidate.candidate_participated.items(),
                        key= lambda cv:cv[1], reverse=True)
        return preferred_voting

    def initialize(fname):
        candidate_voters = []
        count_votes = 0
        # Read each voter's in order of preference
        try:
            afile = open(fname, "r")
            for line in afile:
                count_votes = count_votes+1
                if not line.isspace():
                    col_values = [x.strip(" \n") for x in line.split(',')]
                    for i in col_values:
                        candidate_voters.append(i)
            Vote.no_of_votes = count_votes
            return candidate_voters
        except:
            print("*** Trouble loading %s." % fname)


'''
Election polling by calling Candidate and Vote class and performing 
the voting for the candidates.
'''
CANDIDATE_FILE = "candidate.csv" #Change the file name of the candidate, if needed
VOTING_FILE = "voter.csv" #Change the file name of the voters, if needed

total_votes = 0
eliminate_votes = 0
votes_per_candidate = {}
second_round_votes_candidates = {}
votes_sorted = []
second_round_list = []
winner_list = []
winner = ""
first_winner = ""

# Load candidate details from the file
candidate_list = Candidate.initialize(CANDIDATE_FILE)
voters_list = Vote.initialize(VOTING_FILE)

#Elimination votes calculation
eliminate_votes = Vote.no_of_votes//4

#Adding votes from the voting list
for votes in voters_list:
    votes_per_candidate = Candidate.add_vote(votes)
    votes_per = list(votes_per_candidate)
 
#Based on the votes if doesn't qualify for quarter criteria,
#removing the candidates from the dictionary.
for k in votes_per:
    cand_vote = votes_per_candidate[k]
    if cand_vote < eliminate_votes:
        Candidate.candidate_participated.pop(k)

#Sorting the candidates with most number of votes
votes_sorted.append(Vote.most_preferred(votes_per))
for vot in votes_sorted:
    first_winner = vot[0]

print("The winner of the first round is {} with {} votes ".format(first_winner[0], first_winner[1]))

#Resetting the number of votes for 2nd round
Candidate.clear_votes()

second_round_list = votes_sorted

#Assigning no. of votes as 0 to the sorted voters list from 1st round
for i in second_round_list:
    for cand_sets in i:
        second_round_votes_candidates[cand_sets[0]]=0

#Adding votes after the preference for 2nd round
for pref in voters_list:
    second_round_votes_candidates = Candidate.add_vote(pref)
    second_round_votes = list(second_round_votes_candidates)

winner_list.append(Vote.most_preferred(second_round_votes))

for win in winner_list:
    winner = win[0]

print("The winner of the voting is {} with {} votes ".format(winner[0], winner[1]))