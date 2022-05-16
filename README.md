# downbeat
So downbeat is a simple 2d platformer. Right now, there are many features missing, but it has been built in a very expandable way so that other features can be implemented as I go.

Controls:
Up arrow: Jump, hold for more height
Left arrow: Move Left
Right arrow: Move Right
R: Reset Level



Here is the concept
There is a metronome ticking and whenever it hits the downbeat the gravity changes directions.
The time signature and tempo might change with different levels.

NOTE: Also, make slippery and sticky surfaces in different levels. And jumpy surfaces.

Sprite movement when beat hits
Something special on the beat drop
color changing on the down beat. Maybe becomes photo negative

Example of level layout JSON
[
	{
		"sprite_classname": "DownbeatPlayer",
		"params": {
			"color": "green",
			...
		}
	},
	{
		"sprite_classname": "Wall",

		"params": {
			"height": 50,
			"width": 150
		}
	},
	{
		"sprite_classname": "Wall",
		"params": {
			"height": 100,
			"width": 50
		}
	},
	{
		"sprite_classname": "Spikes",
		"params": {
			"length": 20
		}
	}
]

Write a Scene method that uses the python library to parse the JSON into a list of dictionaries. Then, iterate through the list and call an abstract Scene.createSprite() on each dictionary. The DownbeatScene subclass will implement this method to instantiate sprites based on the given classname and parameters. This will require a switch on sprite_classname.

Yes, converting data to text and then back again through ifs or switches is exactly the code smell I told you about. However, it's acceptable here because there's really no better way to instantiate classes based on a string input, which you need to do because you're encoding data in a string-based format for long-term storage. It's only a code smell if you're converting data to text and back again for no reason.

#original code for registering collisions. I might use this on enemies

		hits = pygame.sprite.spritecollide(self.player1, self.walls, False)
		for wall in hits:
			self.player1.handle_wall_collisions(wall)
			wall.handle_player1_collisions(self.player1)