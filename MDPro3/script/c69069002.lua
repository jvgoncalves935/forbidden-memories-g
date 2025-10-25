--Stocking Anarchy
--c69069002
local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()

	--Treat this card as mentioning "Toon World"
	aux.AddCodeList(c,15259703)

	--Special Summon from hand by sending 2 Extra Deck cards to grave (cost)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id+EFFECT_COUNT_CODE_OATH)
	e1:SetCondition(s.spcon)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)

	--Cannot be used as material (Fusion, Synchro, Link, Ritual). Xyz allowed only for Toon Xyz
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_CANNOT_BE_FUSION_MATERIAL)
	e2:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	e2:SetValue(1)
	c:RegisterEffect(e2)
	local e3=e2:Clone()
	e3:SetCode(EFFECT_CANNOT_BE_SYNCHRO_MATERIAL)
	c:RegisterEffect(e3)
	local e4=Effect.CreateEffect(c)
	e4:SetType(EFFECT_TYPE_SINGLE)
	e4:SetCode(EFFECT_CANNOT_BE_XYZ_MATERIAL)
	e4:SetProperty(EFFECT_FLAG_CANNOT_DISABLE+EFFECT_FLAG_UNCOPYABLE)
	-- allow Xyz only if the Xyz is Toon
	e4:SetValue(function(e,c)
		if not c then return false end
		return not (c:IsType(TYPE_XYZ) and c:IsType(TYPE_TOON))
	end)
	c:RegisterEffect(e4)
	local e5=e2:Clone()
	e5:SetCode(EFFECT_CANNOT_BE_LINK_MATERIAL)
	c:RegisterEffect(e5)
	local e6=e2:Clone()
	e6:SetCode(EFFECT_CANNOT_BE_RITUAL_MATERIAL)
	c:RegisterEffect(e6)

	--Direct attack condition (Toon World or Mundo da PUTARIA)
	local e7=Effect.CreateEffect(c)
	e7:SetType(EFFECT_TYPE_SINGLE)
	e7:SetCode(EFFECT_DIRECT_ATTACK)
	e7:SetCondition(s.dircon)
	c:RegisterEffect(e7)

	--Add 1 "Anarchy" monster to hand when Summoned (Deck/Grave/Removed), except self
	local e8=Effect.CreateEffect(c)
	e8:SetDescription(aux.Stringid(id,1))
	e8:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e8:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e8:SetCode(EVENT_SUMMON_SUCCESS)
	e8:SetCountLimit(1,id)
	e8:SetTarget(s.thtg)
	e8:SetOperation(s.thop)
	c:RegisterEffect(e8)
	local e9=e8:Clone()
	e9:SetCode(EVENT_SPSUMMON_SUCCESS)
	c:RegisterEffect(e9)
	local e10=e8:Clone()
	e10:SetCode(EVENT_FLIP_SUMMON_SUCCESS)
	c:RegisterEffect(e10)

	--Banish from opponent Extra Deck (battle trigger)
	local e11=Effect.CreateEffect(c)
	e11:SetDescription(aux.Stringid(id,2))
	e11:SetCategory(CATEGORY_REMOVE)
	e11:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e11:SetCode(EVENT_BATTLE_CONFIRM)
	e11:SetCountLimit(1,id)
	e11:SetTarget(s.rmexdtg)
	e11:SetOperation(s.rmexdop)
	c:RegisterEffect(e11)

	--Banish from opponent Extra Deck (after opponent monster effect resolves) — window after resolution
	local e12=Effect.CreateEffect(c)
	e12:SetDescription(aux.Stringid(id,2))
	e12:SetCategory(CATEGORY_REMOVE)
	e12:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_O)
	e12:SetCode(EVENT_CHAIN_SOLVED)
	e12:SetProperty(EFFECT_FLAG_DELAY)
	e12:SetRange(LOCATION_MZONE)
	e12:SetCountLimit(1,id)
	e12:SetCondition(s.rmexdcon)
	e12:SetTarget(s.rmexdtg)
	e12:SetOperation(s.rmexdop)
	c:RegisterEffect(e12)
end

-- Special Summon cost filter: any card able to be sent to GY
function s.cfilter(c)
	return c:IsAbleToGraveAsCost()
end

function s.spcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	-- Need at least 2 cards in Extra Deck to pay cost
	return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.GetMatchingGroupCount(Card.IsAbleToGrave,tp,LOCATION_EXTRA,0,nil)>=2
end

-- target: select exactly 2 cards from Extra Deck as cost (single selection window)
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
	if chk==0 then return true end
	local g=Duel.GetMatchingGroup(Card.IsAbleToGrave,tp,LOCATION_EXTRA,0,nil)
	if #g<2 then return false end
	Duel.SetOperationInfo(0,CATEGORY_TOGRAVE,nil,2,tp,LOCATION_EXTRA)
	return true
end

-- operation: send 2 cards as COST
function s.spop(e,tp,eg,ep,ev,re,r,rp,c)
	local g=Duel.GetMatchingGroup(Card.IsAbleToGrave,tp,LOCATION_EXTRA,0,nil)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
	local sg=g:SelectSubGroup(tp,aux.dncheck,false,2,2)
	if sg and #sg==2 then
		Duel.SendtoGrave(sg,REASON_COST)
	end
	-- apply global summon ban for rest of duel
	local hc = c or e:GetHandler()
	s.register_summon_ban(hc,tp)
end

-- Direct attack condition (checks for Toon World or Mundo da PUTARIA)
function s.dircon(e)
	local tp=e:GetHandlerPlayer()
	return Duel.IsExistingMatchingCard(function(cc)
		return cc:IsFaceup() and (cc:IsCode(15259703) or cc:IsCode(69069069))
	end, tp, LOCATION_ONFIELD, 0, 1, nil)
end

-- Search Anarchy (Deck/Grave/Removed)
function s.thfilter(c)
	return c:IsSetCard(0xf6f) and c:IsType(TYPE_MONSTER) and not c:IsCode(id) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED)
end
function s.thop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,0,1,1,nil)
	if #g>0 then
		Duel.SendtoHand(g,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,g)
	end
	-- apply global summon ban for rest of duel
	s.register_summon_ban(e:GetHandler(),tp)
end

-- Banish from opponent Extra Deck implementation
function s.rmfilter(c,tp)
	return c:IsAbleToRemove(tp,POS_FACEDOWN)
end
function s.rmexdcon(e,tp,eg,ep,ev,re,r,rp)
	-- triggered when a chain resolved that was activated by opponent and was a monster effect, excluding Damage Step
	return rp==1-tp and re:IsActiveType(TYPE_MONSTER) and not Duel.IsDamageCalculated()
end
function s.rmexdtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(s.rmfilter,tp,0,LOCATION_EXTRA,1,nil,tp) end
	Duel.SetOperationInfo(0,CATEGORY_REMOVE,nil,1,1-tp,LOCATION_EXTRA)
end
function s.rmexdop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetFieldGroup(tp,0,LOCATION_EXTRA)
	if #g==0 then return end
	Duel.ConfirmCards(tp,g,true)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local sg=g:FilterSelect(tp,s.rmfilter,1,1,nil,tp)
	if #sg>0 then
		Duel.Remove(sg,POS_FACEDOWN,REASON_EFFECT)
	end
	Duel.ShuffleExtra(1-tp)
	-- apply global summon ban (because an effect of this card was activated)
	s.register_summon_ban(e:GetHandler(),tp)
end

-- register global summon-ban for player 'p' for rest of duel
function s.register_summon_ban(c,p)
	if Duel.GetFlagEffect(p,id+1000)~=0 then return end
	Duel.RegisterFlagEffect(p,id+1000,0,0,1)
	-- cannot Normal Summon (except Universo G / Toon)
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_CANNOT_SUMMON)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e1:SetTargetRange(1,0)
	e1:SetTarget(s.splimit_all)
	Duel.RegisterEffect(e1,p)
	-- cannot Special Summon (except Universo G / Toon)
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e2:SetTargetRange(1,0)
	e2:SetTarget(s.splimit_all)
	Duel.RegisterEffect(e2,p)
	-- cannot Flip Summon (except Universo G / Toon)
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_FIELD)
	e3:SetCode(EFFECT_CANNOT_FLIP_SUMMON)
	e3:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e3:SetTargetRange(1,0)
	e3:SetTarget(s.splimit_all)
	Duel.RegisterEffect(e3,p)
end

-- global splimit: blocks summons except Universo G (0xc50) or Toon
function s.splimit_all(e,c,sump,sumtype,sumpos,targetp,se)
	if not c then return false end
	return not (c:IsSetCard(0xc50) or c:IsType(TYPE_TOON))
end
