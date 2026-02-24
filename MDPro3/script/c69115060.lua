--Coringa Dano
local s,id=GetID()
function s.initial_effect(c)

	-- Xyz Summon procedure
	aux.AddXyzProcedureLevelFree(c,s.xyzfilter,s.xyzcheck,2,2)
	c:EnableReviveLimit()

	-- This card becomes "Alexandre Senna" on the field
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetCode(EFFECT_CHANGE_CODE)
	e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
	e1:SetRange(LOCATION_MZONE)
	e1:SetValue(69115001)
	c:RegisterEffect(e1)

	-- Quick Effect: detach, mill 3, bounce 1-2
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,2))
	e2:SetCategory(CATEGORY_TOGRAVE+CATEGORY_TOHAND)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetCode(EVENT_FREE_CHAIN)
	e2:SetRange(LOCATION_MZONE)
	e2:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_END_PHASE)
	e2:SetCountLimit(1,id)
	e2:SetCost(s.bcost)
	e2:SetTarget(s.btg)
	e2:SetOperation(s.bop)
	c:RegisterEffect(e2)

	-- Ignition: detach, search
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,3))
	e3:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e3:SetType(EFFECT_TYPE_IGNITION)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCountLimit(1,id+200)
	e3:SetCost(s.bcost)
	e3:SetTarget(s.thtg)
	e3:SetOperation(s.thop)
	c:RegisterEffect(e3)

end

function s.xyzfilter(c)
	return c:IsFaceup()
		and c:IsSetCard(0xc50)
		and c:IsType(TYPE_MONSTER)
end

-- Xyz material restriction
-- 1 Level 4 or lower + 1 any level
-- both Universo G
function s.xyzcheck(g,lc,tp)
	if g:GetCount()~=2 then return false end

	local tc1=g:GetFirst()
	local tc2=g:GetNext(tc1)
	if not tc1 or not tc2 then return false end

	-- ambos precisam ter Level válido
	if tc1:GetLevel()<=0 or tc2:GetLevel()<=0 then
		return false
	end

	-- ambos devem ser Universo G
	if not (tc1:IsSetCard(0xc50) and tc2:IsSetCard(0xc50)) then
		return false
	end

	-- pelo menos 1 deve ser Level 4 EXATO
	return tc1:IsLevel(4) or tc2:IsLevel(4)
end

-- Shared detach cost
function s.bcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():CheckRemoveOverlayCard(tp,1,REASON_COST) end
	e:GetHandler():RemoveOverlayCard(tp,1,1,REASON_COST)
end

-- Quick Effect: mill 3, bounce 1-2
function s.btg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetDecktopGroup(tp,3):GetCount()>0
			and Duel.IsExistingMatchingCard(s.bfilter,tp,
				LOCATION_ONFIELD+LOCATION_GRAVE,
				LOCATION_ONFIELD+LOCATION_GRAVE,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOGRAVE,nil,3,tp,LOCATION_DECK)
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,PLAYER_ALL,
		LOCATION_ONFIELD+LOCATION_GRAVE)
end

function s.bfilter(c)
	return c:IsAbleToHand()
end

function s.bop(e,tp,eg,ep,ev,re,r,rp)

	-- Mill 3
	Duel.DiscardDeck(tp,3,REASON_EFFECT)

	-- Seleciona 1 até 2
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
	local g=Duel.SelectMatchingCard(
		tp,s.bfilter,tp,
		LOCATION_ONFIELD+LOCATION_GRAVE,
		LOCATION_ONFIELD+LOCATION_GRAVE,
		1,2,nil
	)
	if #g>0 then
		Duel.SendtoHand(g,nil,REASON_EFFECT)
	end
end

-- Ignition: search Universo G S/T
function s.thfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_SPELL+TYPE_TRAP)
		and c:IsAbleToHand()
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(
			s.thfilter,tp,LOCATION_DECK,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end

function s.thop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_DECK,0,1,1,nil)
	if #g>0 then
		Duel.SendtoHand(g,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,g)
	end
end