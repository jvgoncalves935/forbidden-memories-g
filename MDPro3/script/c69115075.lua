-- Xaropinho de Família
local s,id=GetID()

function s.initial_effect(c)

	-- Special Summon from hand (Quick Effect)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id) -- hard once per turn
	e1:SetCondition(s.spcon)
	e1:SetCost(s.spcost)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)

	-- Effect on Summon
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,3))
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCode(EVENT_SUMMON_SUCCESS)
	e2:SetCountLimit(1,id+100) -- hard once per turn
	e2:SetTarget(s.lktg)
	e2:SetOperation(s.lkop)
	c:RegisterEffect(e2)

	local e2b=e2:Clone()
	e2b:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e2b)

	local e2c=e2:Clone()
	e2c:SetCode(EVENT_FLIP_SUMMON_SUCCESS)
	c:RegisterEffect(e2c)
end

function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	local banished=Duel.GetFieldGroupCount(tp,LOCATION_REMOVED,LOCATION_REMOVED)
	local deckcount=Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)
	return banished>=2 or deckcount>=2
end

function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local banished=Duel.GetFieldGroupCount(tp,LOCATION_REMOVED,LOCATION_REMOVED)
		local deckcount=Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)
		return banished>=2 or deckcount>=2
	end

	local can_return=Duel.GetFieldGroupCount(tp,LOCATION_REMOVED,LOCATION_REMOVED)>=2
	local can_banish=Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>=2
	local opt=0

	if can_return and can_banish then
		opt=Duel.SelectOption(
			tp,
			aux.Stringid(id,1), -- Retornar 2 cards banidos
			aux.Stringid(id,2)  -- Banir 2 cards do topo do Deck
		)
	elseif can_return then
		opt=0
	else
		opt=1
	end

	if opt==0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
		local g=Duel.SelectMatchingCard(
			tp,Card.IsAbleToDeck,tp,
			LOCATION_REMOVED,LOCATION_REMOVED,
			2,2,nil
		)
		Duel.SendtoDeck(g,nil,SEQ_DECKSHUFFLE,REASON_COST)
	else
		Duel.Remove(
			Duel.GetDecktopGroup(tp,2),
			POS_FACEUP,
			REASON_COST
		)
	end
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and e:GetHandler():IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,0,0)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
end

-- Universo G monster (não-Synchro, Level 4 ou menos)
function s.effilter(c,e,tp)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_MONSTER)
		and not c:IsType(TYPE_SYNCHRO)
		and c:IsLevelBelow(4)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

-- Universo G Normal Monster
function s.normfilter(c,e,tp)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_NORMAL)
		and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
end

-- Link Universo G até Link 4
function s.linkfilter(c,e,tp,mg)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_LINK)
		and c:GetLink()<=4
		and c:IsLinkSummonable(mg)
end

function s.lktg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		local ct=Duel.GetLocationCount(tp,LOCATION_MZONE)
		if ct<=0 then return false end

		local can_eff=Duel.IsExistingMatchingCard(
			s.effilter,tp,LOCATION_DECK+LOCATION_HAND,0,1,nil,e,tp
		)

		local can_norm=Duel.IsExistingMatchingCard(
			s.normfilter,tp,LOCATION_DECK+LOCATION_HAND,0,1,nil,e,tp
		)

		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
		local can_link=Duel.IsExistingMatchingCard(
			s.linkfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,mg
		)

		return can_eff or (can_norm and can_link)
	end
end

function s.lkop(e,tp,eg,ep,ev,re,r,rp)
	local ct=Duel.GetLocationCount(tp,LOCATION_MZONE)
	if ct<=0 then return end

	local can_eff=Duel.IsExistingMatchingCard(
		s.effilter,tp,LOCATION_DECK+LOCATION_HAND,0,1,nil,e,tp
	)

	local can_norm=Duel.IsExistingMatchingCard(
		s.normfilter,tp,LOCATION_DECK+LOCATION_HAND,0,1,nil,e,tp
	)

	local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
	local can_link=Duel.IsExistingMatchingCard(
		s.linkfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp,mg
	)

	local opt=0
	if can_eff and can_norm and can_link then
		opt=Duel.SelectOption(
			tp,
			aux.Stringid(id,4),
			aux.Stringid(id,5)
		)
	elseif can_eff then
		opt=0
	else
		opt=1
	end

	if opt==0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local tc=Duel.SelectMatchingCard(
			tp,s.effilter,tp,LOCATION_DECK+LOCATION_HAND,0,1,1,nil,e,tp
		):GetFirst()
		if not tc then return end

		if Duel.SpecialSummon(tc,0,tp,tp,false,false,POS_FACEUP)==0 then return end

		local e1=Effect.CreateEffect(e:GetHandler())
		e1:SetType(EFFECT_TYPE_SINGLE)
		e1:SetCode(EFFECT_DISABLE)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD)
		tc:RegisterEffect(e1)

		local e2=e1:Clone()
		e2:SetCode(EFFECT_DISABLE_EFFECT)
		tc:RegisterEffect(e2)
	else
		local max=math.min(2,ct)
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local g=Duel.SelectMatchingCard(
			tp,s.normfilter,tp,LOCATION_DECK+LOCATION_HAND,0,1,max,nil,e,tp
		)
		if #g==0 then return end

		Duel.SpecialSummon(g,0,tp,tp,false,false,POS_FACEUP)
		Duel.BreakEffect()

		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local sc=Duel.SelectMatchingCard(
			tp,s.linkfilter,tp,LOCATION_EXTRA,0,1,1,nil,e,tp,mg
		):GetFirst()
		if not sc then return end

		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_LINK)
		local mat=mg:Select(tp,sc:GetLink(),sc:GetLink(),nil)

		sc:SetMaterial(mat)
		Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_LINK)

		if Duel.SpecialSummon(sc,SUMMON_TYPE_LINK,tp,tp,false,false,POS_FACEUP)>0 then
			sc:CompleteProcedure()
		end

		local e1=Effect.CreateEffect(e:GetHandler())
		e1:SetType(EFFECT_TYPE_FIELD)
		e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
		e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
		e1:SetTargetRange(1,0)
		e1:SetTarget(s.linklock)
		e1:SetReset(RESET_PHASE+PHASE_END)
		Duel.RegisterEffect(e1,tp)
	end
end

function s.linklock(e,c,tp,sumtp,sumpos)
	return sumtp&SUMMON_TYPE_LINK~=0
end
