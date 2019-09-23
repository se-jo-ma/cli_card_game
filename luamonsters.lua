--Player Class
player = {elx=0,turn=false}
function player:new (o)
	o = o or {}
	setmetatable(o, self)
	self.__index = self
	return o
end

p1 = player:new()
p2 = player:new()

--Deck Class
deck = {}
function deck:new (o)
	o = o or {}
	setmetatable(o, self)
	self.__index = self
	return o
end

function shuffle(deck)
	size = #deck
	for i = size, 1, -1 do
		local rand = math.random(i)
		deck[i], deck[rand] = deck[rand], deck[i]
	end
	return tbl
end

function displayDeckChoices(a)
	print(a.." which deck would you like to play with?")
	print("Deck 1: "..deck1())
	print("Deck 2: "..deck2())
	print("Deck 3: "..deck3())
	print("------------------------------------------------")
end

function deckChoice()
	local inp = io.read()
	if inp == 1 then return deck1()
	elseif inp == 2 then return deck2()
	elseif inp == 3 then return deck3()
	end
end

monDeck = deck:new()
itemDeck = deck:new()

--Hand Class
hand = {}
function hand:new (o)
	o = o or {}
	setmetatable(o, self)
	self.__index = self
	return o
end

function handPrint(hand)
	if hand[1] == nil then print("Empty hand")
	elseif hand[2] == nil then print("|"..hand[1].name.."|")
	elseif hand[3] == nil then print("|"..hand[1].name.."| |"..hand[2].name.."|")
	else
		print("|"..hand[1].name.."| |"..hand[2].name.."| |"..hand[3].name.."|")
	end
end

monHand = hand:new()
itemHand = hand:new()

--Draw Functions
function etDraw(hand,deck)
end

--Card Class
card = {name = "",type = "",cost=0,lvl=1}
function card:new (o)
	o = o or {}
	setmetatable(o, self)
	self.__index = self
	return o
end
function card:getName()
	return self.name
end
function card:getType()
	return self.type
end
function card:getCost()
	return self.cost
end
function card:getLevel()
	return self.lvl
end

--Monster Card Sub Class
monster = card:new{type="Monster"}
function monster:getHP()
	return self.hp
end
function monster:getPos()
	return self.pos
end
function monster:getW1()
	return self.w1 or nil
end
function monster:getW1Atk()
	return self.w1atk or nil
end
function monster:getW2()
	return self.w2 or nil
end
function monster:getW2Atk()
	return self.w2atk or nil
end
function monster:getW3()
	return self.w3 or nil
end
function monster:getW3Atk()
	return self.w3atk or nil
end
function monster:getGHVal()
	return self.ghval or nil
end
function monster:getHealVal()
	return self.hval or nil
end

--Spell Card Sub Class
spell = card:new{type="Spell"}
function spell:getTarget()
	return self.tar
end
function spell:getTargetNumber()
	return self.tarnum
end
function spell:getDmg()
	return self.dmg or nil
end
function spell:getHeal()
	return self.heal or nil
end
function spell:getEffect()
	return self.effect or nil
end

--Equipment Card Sub Class
equip = card:new{type="Equipment"}
function equip:getTarget()
	return self.tar
end
function equip:getArmor()
	return self.armor or nil
end
function equip:getWeapon()
	return self.wpn or nil
end
function equip:getWpnAttack()
	return self.wpnatk or nil
end
--Board
board = {}
for i=1,2 do
	board[i] = {}
	for j=1,3 do
		board[i][j] = monster:new{name="Empty"}
	end
end
function boardPrint()
	print(board[1][1].name.." | "..board[1][2].name.." | "..board[1][3].name)
	print("---------------------")
	print(board[2][1].name.." | "..board[2][2].name.." | "..board[2][3].name)
end
--Misc Functions
function coinFlip()
	local a = math.random(1,2)
	print("After a coin was flipped it was decided that Player "..a.." will go first.")
	if a == 1 then p1.turn = true
	else p2.turn = true
	end
end
function playCard(inp,hand,player)
	local i = tonumber(inp)
	print("Playing "..hand[i].name)
	if i == 1 then
		player.elx = player.elx - hand[1].cost
		boardPlace(player,hand[1])
		table.remove(hand,1)
	elseif i == 2 then
		player.elx = player.elx - hand[2].cost
		boardPlace(plaher,hand[2])
		table.remove(hand,2)
	elseif i == 3 then
		player.elx = player.elx - hand[3].cost
		boardPlace(player,hand[3])
		table.remove(hand,3)
	else print("You fuck")
	end
end
function boardPlace(player,mon)
	local a
	if player == p1 then a = 1
	else a = 2
	end
	if board[a][2].name == "Empty" then board[a][2] = mon
	elseif board[a][1].name == "Empty" then board[a][1] = mon
	elseif board[a][3].name == "Empty" then board[a][3] = mon
	end
end
function attack(player)
	return 0
end
function turn(player) -- Missing End Turn Draw and Attack
	player.elx = player.elx + 3
	boardPrint()
	print("You have "..player.elx.." elixir.")
	local inp
	if player == p1 then
		handPrint(p1hand)
		inp = io.read()
		while inp ~= "end" do
			playCard(inp,p1hand,p1)
			boardPrint()
			print("You have "..player.elx.." elixir.")
			handPrint(p1hand)
			inp = io.read()
		end
		etDraw(p1hand,deck1)
		attack(player)
		p1.turn = false
		p2.turn = true
	else
		while inp ~= "end" do
			handPrint(p2hand)
			inp = io.read()
			playCard(inp,p2hand,p2)
			boardPrint()
			print("You have "..player.elx.." elixir.")
			handPrint(p2hand)
			inp = io.read()
		end
		attack(player)
		p1.turn = true
		p2.turn = false
	end
end

--Monster Creation
function gob()
	local a = monster:new{name="Goblin",cost=1,hp=2,w1="bow",w1atk=2}
	return a
end
function knight()
	local a = monster:new{name="Knight",cost=2,hp=4,w1="sword",w1atk=1}
	return a
end
function cleric()
	local a = monster:new{name="Cleric",cost=3,hp=6,ghval = 1,hval = 1}
	return a
end
function blob()
	local a = monster:new{name="Da Blob",cost=3,hp=3,w1="sword",w1atk=1,w2="magic",w2atk=1}
	return a
end

--Spell Creation
function zap()
	local a = spell:new{name="Zap",cost=2,tar="opp",tarnum=1,dmg=3}
	return a
end

--Armor Creation
function shield()
	local a = equip:new{name="Shield", cost=1, armor=3}
	return a
end

--Deck Creation
deck1 =  deck:new{gob(),gob(),knight(),knight(),cleric(),cleric(),zap(),zap(),shield(),shield()}
deck2 =  deck:new{blob(),blob(),knight(),knight(),cleric(),cleric(),zap(),zap(),shield(),shield()}
--
--Start Game
--
-- Player 1 chooses deck
--  displayDeckChoices("Player 1")
--  p1deck = deckChoice()

-- Player 2 chooses deck
--  displayDeckChoices("Player 2")
--  p2deck = deckChoice()

--Shuffle Decks
shuffle(deck1)
shuffle(deck2)

coinFlip() --Coin Flip

--Initial Draw
p1hand = {table.remove(deck1,1),table.remove(deck1,2),table.remove(deck1,3)}
p2hand = {table.remove(deck2,1),table.remove(deck2,2),table.remove(deck2,3)}

--Turns
while deck1 ~= nil and deck2 ~= nil do
	while p1.turn == true do
		turn(p1)
	end
	while p2.turn == true do
		turn(p2)
	end
end
