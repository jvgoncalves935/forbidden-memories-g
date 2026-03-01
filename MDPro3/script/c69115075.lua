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
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCode(EVENT_SUMMON_SUCCESS)
	e2:SetCountLimit(1,id+200) -- hard once per turn
	e2:SetTarget(s.lktg)
	e2:SetOperation(s.lkop)
	c:RegisterEffect(e2)

	local e2b=e2:Clone()
	e2b:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e2b)

	local e2c=e2:Clone()
	e2c:SetCode(EVENT_FLIP_SUMMON_SUCCESS)
	c:RegisterEffect(e2c)

	-- Quick no GY
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,6))
	e3:SetCategory(CATEGORY_TODECK+CATEGORY_DRAW)
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetCode(EVENT_FREE_CHAIN)
	e3:SetRange(LOCATION_GRAVE)
	e3:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e3:SetCountLimit(1,id+400,EFFECT_COUNT_CODE_OATH)
	e3:SetCost(s.gycost)
	e3:SetTarget(s.gytg)
	e3:SetOperation(s.gyop)
	c:RegisterEffect(e3)

	-- Se usado como matéria
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,7))
	e4:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e4:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e4:SetCode(EVENT_BE_MATERIAL)
	e4:SetProperty(EFFECT_FLAG_DELAY)
	e4:SetCountLimit(1,id+600,EFFECT_COUNT_CODE_OATH)
	e4:SetCondition(s.matcon)
	e4:SetTarget(s.mattg)
	e4:SetOperation(s.matop)
	c:RegisterEffect(e4)

end

function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return false end
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
			aux.Stringid(id,2), -- Retornar 2 cards banidos
			aux.Stringid(id,3)  -- Banir 2 cards do topo do Deck
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
		and not c:IsType(TYPE_TUNER)
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
function s.linkfilter(c,e,tp,g)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_LINK)
		and c:GetLink()<=4
		and Duel.GetLocationCountFromEx(tp,tp,g,c)>0
		and c:IsLinkSummonable(g,nil,#g,#g)
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

		return can_eff or can_norm
	end

	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_DECK+LOCATION_HAND)
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

	local opt=0
	if can_eff and can_norm then
		opt=Duel.SelectOption(tp,aux.Stringid(id,4),aux.Stringid(id,5))
	elseif can_eff then
		opt=0
	else
		opt=1
	end

	local summoned=Group.CreateGroup()

	-- SPECIAL SUMMON STEP MODE
	if opt==0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
		local tc=Duel.SelectMatchingCard(
			tp,s.effilter,tp,LOCATION_DECK+LOCATION_HAND,0,1,1,nil,e,tp
		):GetFirst()
		if not tc then return end

		Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP)
		summoned:AddCard(tc)

		-- nega efeitos
		local e1=Effect.CreateEffect(e:GetHandler())
		e1:SetType(EFFECT_TYPE_SINGLE)
		e1:SetCode(EFFECT_DISABLE)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD+RESET_PHASE+PHASE_END)
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

		for tc in aux.Next(g) do
			Duel.SpecialSummonStep(tc,0,tp,tp,false,false,POS_FACEUP)
		end
		summoned:Merge(g)
	end

	Duel.SpecialSummonComplete()

	-- grupo realmente invocado
	local og=Duel.GetOperatedGroup()

	Duel.AdjustAll()

	-- se algo não ficou no campo, cancela
	if og:FilterCount(Card.IsLocation,nil,LOCATION_MZONE)~=og:GetCount() then
		return
	end

	-- LINK SUMMON (manual)
	-- todos os monstros face-up no seu campo podem ser considerados
	local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

	-- Links possíveis considerando o campo atual
	local exg=Duel.GetMatchingGroup(function(c)
		return c:IsSetCard(0xc50)
			and c:IsType(TYPE_LINK)
			and c:GetLink()<=4
			and c:IsLinkSummonable(mg)
	end,tp,LOCATION_EXTRA,0,nil)

	if #exg==0 then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sc=exg:Select(tp,1,1,nil):GetFirst()
	if not sc then return end

	-- selecionar materiais válidos segundo a própria procedure do Link
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_LINK)
	local mat=mg:SelectSubGroup(tp,function(g)
			return sc:IsLinkSummonable(g)
		end,false,1,sc:GetLink())

	if not mat then return end

	-- checagem de zona do Extra
	if Duel.GetLocationCountFromEx(tp,tp,mat,sc)<=0 then return end

	sc:SetMaterial(mat)

	-- enviar matérias ao GY como material de Link
	Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_LINK)

	-- invocar manualmente
	Duel.SpecialSummon(sc,SUMMON_TYPE_LINK,tp,tp,false,false,POS_FACEUP)
	sc:CompleteProcedure()

	-- lock de Link
	local e1=Effect.CreateEffect(e:GetHandler())
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e1:SetTargetRange(1,0)
	e1:SetTarget(function(e,c)
		return c:IsType(TYPE_LINK)
	end)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)
end

function s.linkmatfilter(g,sc)
	return sc:IsLinkSummonable(g)
end

function s.gycost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsAbleToRemoveAsCost() end
	Duel.Remove(e:GetHandler(),POS_FACEUP,REASON_COST)
end

function s.tdfilter(c)
	return c:IsAbleToDeck()
end

function s.gytg(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsLocation(LOCATION_REMOVED) and s.tdfilter(chkc) end
	if chk==0 then
		return Duel.IsExistingTarget(s.tdfilter,tp,LOCATION_REMOVED,LOCATION_REMOVED,1,nil)
	end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local g=Duel.SelectTarget(tp,s.tdfilter,tp,LOCATION_REMOVED,LOCATION_REMOVED,1,2,nil)
	Duel.SetOperationInfo(0,CATEGORY_TODECK,g,#g,0,0)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,1-tp,1)
end

function s.gyop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
	if not g then return end
	
	local sg=g:Filter(Card.IsRelateToEffect,nil,e)
	local ct=#sg

	if ct>0 then
		Duel.SendtoDeck(sg,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
	end

	if ct>0 and Duel.GetFieldGroupCount(1-tp,LOCATION_DECK,0)>=ct then
		Duel.Draw(1-tp,ct,REASON_EFFECT)
	end
end

function s.matcon(e,tp,eg,ep,ev,re,r,rp)
	local r=e:GetHandler():GetReason()
	return (r&REASON_SYNCHRO~=0)
		or (r&REASON_FUSION~=0)
		or (r&REASON_LINK~=0)
end

function s.thfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_SPELL+TYPE_TRAP)
		and c:IsAbleToHand()
end

function s.mattg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end

function s.matop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local tc=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_DECK,0,1,1,nil):GetFirst()
	if tc then
		Duel.SendtoHand(tc,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,tc)
	end
end
