class Marble:
    def __init__(self, id, prev=None, next=None):
        self.id = id
        self.prev = prev
        self.next = next

    def __repr__(self):
        return f'Marble {self.id}'


class MarbleGame:
    def __init__(self, num_players):
        self.num_players = num_players
        self.marble_id = 1
        initial = Marble(0)
        initial.next = initial
        initial.prev = initial
        self.initial = initial
        self.active = initial
        self.player_scores = {p: 0 for p in range(1, num_players+1)}

    def play_next(self):
        if self.marble_id % 23 == 0:
            player_id = self.marble_id % self.num_players
            player_id = self.num_players if player_id == 0 else player_id
            to_remove = self.active.prev.prev.prev.prev.prev.prev.prev
            # update scores
            self.player_scores[player_id] += self.marble_id + to_remove.id
            self.active = to_remove.next
            # set up references
            to_remove.prev.next, to_remove.next.prev = to_remove.next, to_remove.prev
            self.marble_id += 1

        else:
            m = Marble(self.marble_id)
            # set up references
            m.prev = self.active.next
            m.next = self.active.next.next
            self.active.next.next.prev, self.active.next.next = m, m
            self.active = m
            self.marble_id += 1

    def get_max_score(self):
        return max(self.player_scores.values())


# p1
nsteps = 71010
nplayers = 468

game = MarbleGame(nplayers)
for step in range(nsteps):
    game.play_next()
print(game.get_max_score())

# p2
nsteps = 71010*100
nplayers = 468

game = MarbleGame(nplayers)
for step in range(nsteps):
    game.play_next()
print(game.get_max_score())
