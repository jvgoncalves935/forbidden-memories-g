--Akuma de Família
local s,id=GetID()

function s.initial_effect(c)
	-- Effect 1: SP Summon from hand (Quick Effect, Main Phase only)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetHintTiming(0,TIMING_MAIN_END)
	e1:SetCountLimit(1,id)
	e1:SetCondition(s.spcon)
	e1:SetCost(s.spcost)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)

	-- Effect 2: DIVINE - destroy or SS Universo G
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,4))
	e2:SetCategory(CATEGORY_DESTROY+CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetCode(EVENT_FREE_CHAIN)
	e2:SetRange(LOCATION_MZONE)
	e2:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
	e2:SetCountLimit(1,id+200)
	e2:SetCondition(s.mainphasecon)
	e2:SetCost(s.divcost)
	e2:SetTarget(s.divtg)
	e2:SetOperation(s.divop)
	c:RegisterEffect(e2)

	-- Effect 3: FIRE & WATER - excavate 7, add 1 monster to hand, rest to bottom
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,5))
	e3:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetCode(EVENT_FREE_CHAIN)
	e3:SetRange(LOCATION_MZONE)
	e3:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
	e3:SetCountLimit(1,id+400)
	e3:SetCondition(s.mainphasecon)
	e3:SetCost(s.fwcost)
	e3:SetTarget(s.fwtg)
	e3:SetOperation(s.fwop)
	c:RegisterEffect(e3)

	-- Effect 4: EARTH & WIND - opponent gives control of Extra Deck monster
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,6))
	e4:SetCategory(CATEGORY_CONTROL)
	e4:SetType(EFFECT_TYPE_QUICK_O)
	e4:SetCode(EVENT_FREE_CHAIN)
	e4:SetRange(LOCATION_MZONE)
	e4:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
	e4:SetCountLimit(1,id+600)
	e4:SetCondition(s.mainphasecon)
	e4:SetCost(s.ewcost)
	e4:SetTarget(s.ewtg)
	e4:SetOperation(s.ewop)
	c:RegisterEffect(e4)

	-- Effect 5: LIGHT & DARK - banish 2 cards of different types from any GY
	local e5=Effect.CreateEffect(c)
	e5:SetDescription(aux.Stringid(id,7))
	e5:SetCategory(CATEGORY_REMOVE)
	e5:SetType(EFFECT_TYPE_QUICK_O)
	e5:SetCode(EVENT_FREE_CHAIN)
	e5:SetRange(LOCATION_MZONE)
	e5:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
	e5:SetCountLimit(1,id+800)
	e5:SetCondition(s.mainphasecon)
	e5:SetCost(s.ldcost)
	e5:SetTarget(s.ldtg)
	e5:SetOperation(s.ldop)
	c:RegisterEffect(e5)
end

-- Main Phase only condition (shared by all field Quick Effects)
function s.mainphasecon(e,tp,eg,ep,ev,re,r,rp)
	local ph=Duel.GetCurrentPhase()
	return ph==PHASE_MAIN1 or ph==PHASE_MAIN2
end

-- CHAIN LOCK: only 1 effect per chain (shared across all effects)
function s.chainlock_check(tp)
	return Duel.GetFlagEffect(tp,id)==0
end

function s.chainlock_register(tp)
	Duel.RegisterFlagEffect(tp,id,RESET_CHAIN,0,1)
end

-- EFFECT 1: SP SUMMON FROM HAND
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	local ph=Duel.GetCurrentPhase()
	return ph==PHASE_MAIN1 or ph==PHASE_MAIN2
end

function s.spcostfilter(c)
	return c:IsType(TYPE_MONSTER) and not c:IsPublic()
end

-- Check: 2 revealed monsters have distinct attributes from each other and from this card
function s.spcheck(g,ec)
	local c1=g:GetFirst()
	local c2=g:GetNext()
	if not c1 or not c2 then return false end
	local a1=c1:GetAttribute()
	local a2=c2:GetAttribute()
	local ac=ec:GetAttribute()
	return a1~=a2 and a1~=ac and a2~=ac
end

function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	local g=Duel.GetMatchingGroup(s.spcostfilter,tp,LOCATION_HAND,0,c)
	if chk==0 then return g:CheckSubGroup(s.spcheck,2,2,c) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
	local sg=g:SelectSubGroup(tp,s.spcheck,false,2,2,c)
	Duel.ConfirmCards(1-tp,sg)
	Duel.RaiseEvent(sg,EVENT_CUSTOM+id,e,REASON_COST,tp,tp,0)
	Duel.ShuffleHand(tp)
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
		and s.chainlock_check(tp) end
	s.chainlock_register(tp)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if c:IsRelateToChain() then
		Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
	end
end

-- Reveal 1 DIVINE; opponent destroys 1 of their cards OR you SS 1 Universo G from Deck
function s.divfilter(c)
	return c:IsType(TYPE_MONSTER) and c:IsAttribute(ATTRIBUTE_DIVINE) and not c:IsPublic()
end

function s.divcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(s.divfilter,tp,LOCATION_HAND,0,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
	local g=Duel.SelectMatchingCard(tp,s.divfilter,tp,LOCATION_HAND,0,1,1,nil)
	Duel.ConfirmCards(1-tp,g)
	Duel.RaiseEvent(g,EVENT_CUSTOM+id,e,REASON_COST,tp,tp,0)
	Duel.ShuffleHand(tp)
end

function s.divspfilter(c,e,tp)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_MONSTER)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

function s.divtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local opp=1-tp
	local can_destroy=Duel.IsExistingMatchingCard(aux.TRUE,opp,LOCATION_ONFIELD,0,1,nil)
	local can_ss=Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsExistingMatchingCard(s.divspfilter,tp,LOCATION_DECK,0,1,nil,e,tp)
	if chk==0 then return (can_destroy or can_ss) and s.chainlock_check(tp) end
	s.chainlock_register(tp)
	if can_destroy then
		Duel.SetOperationInfo(0,CATEGORY_DESTROY,nil,1,opp,LOCATION_ONFIELD)
	end
	if can_ss then
		Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_DECK)
	end
end

function s.divop(e,tp,eg,ep,ev,re,r,rp)
	local opp=1-tp
	local can_destroy=Duel.IsExistingMatchingCard(aux.TRUE,opp,LOCATION_ONFIELD,0,1,nil)
	if can_destroy then
		-- Opponent chooses between 2 options
		Duel.Hint(HINT_SELECTMSG,opp,HINTMSG_EFFECT)
		local op=Duel.SelectOption(opp,aux.Stringid(id,2),aux.Stringid(id,3))
		if op==0 then
			-- Option 0: opponent destroys 1 of their cards
			Duel.Hint(HINT_SELECTMSG,opp,HINTMSG_DESTROY)
			local g=Duel.SelectMatchingCard(opp,aux.TRUE,opp,LOCATION_ONFIELD,0,1,1,nil)
			if g:GetCount()>0 then
				Duel.Destroy(g,REASON_EFFECT)
			end
			return
		end
		-- Option 1: you SS Universo G (falls through)
	end
	-- SS 1 Universo G from Deck
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,s.divspfilter,tp,LOCATION_DECK,0,1,1,nil,e,tp)
	if g:GetCount()>0 then
		Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)
	end
end

-- Reveal 1 FIRE + 1 WATER; excavate 7, put 1 on top, draw 1 at End Phase
function s.fwfilter(c)
	return c:IsType(TYPE_MONSTER) and c:IsAttribute(ATTRIBUTE_FIRE+ATTRIBUTE_WATER) and not c:IsPublic()
end

function s.fwcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(s.fwfilter,tp,LOCATION_HAND,0,nil)
	if chk==0 then return g:CheckSubGroup(aux.gfcheck,2,2,Card.IsAttribute,ATTRIBUTE_FIRE,ATTRIBUTE_WATER) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
	local sg=g:SelectSubGroup(tp,aux.gfcheck,false,2,2,Card.IsAttribute,ATTRIBUTE_FIRE,ATTRIBUTE_WATER)
	Duel.ConfirmCards(1-tp,sg)
	Duel.RaiseEvent(sg,EVENT_CUSTOM+id,e,REASON_COST,tp,tp,0)
	Duel.ShuffleHand(tp)
end

-- Filter: monster with attribute not already in player's hand
function s.fwmonfilter(c,handattrs)
	return c:IsType(TYPE_MONSTER) and c:IsAbleToHand()
		and not c:IsAttribute(handattrs)
end

function s.fwtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.GetMatchingGroupCount(aux.TRUE,tp,LOCATION_DECK,0,nil)>0
		and s.chainlock_check(tp) end
	s.chainlock_register(tp)
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end

function s.fwop(e,tp,eg,ep,ev,re,r,rp)
	Duel.ConfirmDecktop(tp,7)
	local g=Duel.GetDecktopGroup(tp,7)
	if #g==0 then return end
	local cnt=#g
	Duel.DisableShuffleCheck()
	-- Build bitmask of attributes already in player's hand
	local handattrs=0
	local hg=Duel.GetMatchingGroup(aux.TRUE,tp,LOCATION_HAND,0,nil)
	local hc=hg:GetFirst()
	while hc do
		handattrs=handattrs|hc:GetAttribute()
		hc=hg:GetNext()
	end
	-- Player selects 1 monster whose attribute is not already in hand
	local sub=g:Filter(s.fwmonfilter,nil,handattrs)
	local sent=0
	if #sub>0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
		local sc=sub:Select(tp,1,1,nil):GetFirst()
		if sc then
			Duel.SendtoHand(sc,nil,REASON_EFFECT)
			Duel.ConfirmCards(1-tp,sc)
			Duel.ShuffleHand(tp)
			sent=1
		end
	end
	-- Put remaining excavated cards to bottom in any order
	local rem=cnt-sent
	if rem>0 then
		Duel.SortDecktop(tp,tp,rem)
		for i=1,rem do
			local dg=Duel.GetDecktopGroup(tp,1)
			if dg and #dg>0 then
				Duel.MoveSequence(dg:GetFirst(),SEQ_DECKBOTTOM)
			end
		end
	end
end

-- Reveal 1 EARTH + 1 WIND; opponent gives control of Fusion/Synchro/Xyz/Link/Ritual until End Phase
function s.ewfilter(c)
	return c:IsType(TYPE_MONSTER) and c:IsAttribute(ATTRIBUTE_EARTH+ATTRIBUTE_WIND) and not c:IsPublic()
end

function s.ewcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(s.ewfilter,tp,LOCATION_HAND,0,nil)
	if chk==0 then return g:CheckSubGroup(aux.gfcheck,2,2,Card.IsAttribute,ATTRIBUTE_EARTH,ATTRIBUTE_WIND) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
	local sg=g:SelectSubGroup(tp,aux.gfcheck,false,2,2,Card.IsAttribute,ATTRIBUTE_EARTH,ATTRIBUTE_WIND)
	Duel.ConfirmCards(1-tp,sg)
	Duel.RaiseEvent(sg,EVENT_CUSTOM+id,e,REASON_COST,tp,tp,0)
	Duel.ShuffleHand(tp)
end

function s.ewmonfilter(c)
	return c:IsType(TYPE_FUSION+TYPE_SYNCHRO+TYPE_XYZ+TYPE_LINK+TYPE_RITUAL)
		and c:IsControlerCanBeChanged() and c:IsFaceup()
end

function s.ewtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return Duel.IsExistingMatchingCard(s.ewmonfilter,tp,0,LOCATION_MZONE,1,nil)
		and Duel.GetMZoneCount(tp,c,tp,LOCATION_REASON_CONTROL)>0
		and s.chainlock_check(tp) end
	s.chainlock_register(tp)
	Duel.SetOperationInfo(0,CATEGORY_CONTROL,nil,1,1-tp,LOCATION_MZONE)
end

function s.ewop(e,tp,eg,ep,ev,re,r,rp)
	local opp=1-tp
	local g=Duel.GetMatchingGroup(s.ewmonfilter,tp,0,LOCATION_MZONE,nil)
	if g:GetCount()==0 or Duel.GetMZoneCount(tp,nil,tp,LOCATION_REASON_CONTROL)<=0 then return end
	-- Opponent selects which qualifying monster to give
	Duel.Hint(HINT_SELECTMSG,opp,HINTMSG_CONTROL)
	local sg=g:Select(opp,1,1,nil)
	if sg:GetCount()>0 then
		local tc=sg:GetFirst()
		Duel.HintSelection(sg)
		Duel.GetControl(tc,tp,PHASE_END,1)
	end
end

-- Reveal 1 LIGHT + 1 DARK; banish 2 cards of different types (Monster/Spell/Trap) from any GY
function s.ldfilter(c)
	return c:IsType(TYPE_MONSTER) and c:IsAttribute(ATTRIBUTE_LIGHT+ATTRIBUTE_DARK) and not c:IsPublic()
end

function s.ldcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local g=Duel.GetMatchingGroup(s.ldfilter,tp,LOCATION_HAND,0,nil)
	if chk==0 then return g:CheckSubGroup(aux.gfcheck,2,2,Card.IsAttribute,ATTRIBUTE_LIGHT,ATTRIBUTE_DARK) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
	local sg=g:SelectSubGroup(tp,aux.gfcheck,false,2,2,Card.IsAttribute,ATTRIBUTE_LIGHT,ATTRIBUTE_DARK)
	Duel.ConfirmCards(1-tp,sg)
	Duel.RaiseEvent(sg,EVENT_CUSTOM+id,e,REASON_COST,tp,tp,0)
	Duel.ShuffleHand(tp)
end

-- At most 1 Monster, 1 Spell, 1 Trap in selection (ensures 2 cards are of different types)
function s.ldfselect(g)
	return g:FilterCount(Card.IsType,nil,TYPE_MONSTER)<=1
		and g:FilterCount(Card.IsType,nil,TYPE_SPELL)<=1
		and g:FilterCount(Card.IsType,nil,TYPE_TRAP)<=1
end

function s.ldremfilter(c)
	return c:IsAbleToRemove(nil,POS_FACEUP,REASON_EFFECT)
end

function s.ldtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local g=Duel.GetMatchingGroup(s.ldremfilter,tp,LOCATION_GRAVE,LOCATION_GRAVE,nil)
		return g:CheckSubGroup(s.ldfselect,2,2) and s.chainlock_check(tp)
	end
	s.chainlock_register(tp)
	Duel.SetOperationInfo(0,CATEGORY_REMOVE,nil,2,0,LOCATION_GRAVE)
end

function s.ldop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetMatchingGroup(s.ldremfilter,tp,LOCATION_GRAVE,LOCATION_GRAVE,nil)
	if not g:CheckSubGroup(s.ldfselect,2,2) then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local sg=g:SelectSubGroup(tp,s.ldfselect,false,2,2)
	if sg and sg:GetCount()>0 then
		Duel.Remove(sg,POS_FACEUP,REASON_EFFECT)
	end
end
