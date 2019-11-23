content='''
TapChief, Shashank’s current venture, is a platform where students and startups can consult industry experts to solve their problems, which are primarily in decision making in the areas of careers, startups, technology, sales and marketing, and finance and legal. Users can either choose an expert to consult on their own or are assisted by the TapChief team on a case-by-case basis, thereby ensuring the best expert to consult for a particular problem.

The startup allows users to come onto the platform and search for an expert by skill, organisation or name, and discover multiple expert profiles. The user can then go on to request a consultation with the expert by suggesting three time slots and an agenda for the same. The expert, who is then notified via email and SMS, can accept, reject or suggest alternate timings for the consultation.
'''
word = 'is'
para = []
para = content.split('\n\n')
dicti={}
for j in range(len(para)):
    data=[]
    indexes = []
    data = para[j].split(' ')
    #print(data)
    for i in range(len(data)):
        if word == data[i]:
            indexes.append(i)

    dicti.update({str(j+1):indexes})
print(dicti)