--Senhor dos Anais
local s,id=GetID()

function s.initial_effect(c)
	c:EnableReviveLimit()

	-- 1) Ritual da mão escavando o Deck do oponente (Quick, HOPT)
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetCountLimit(1,id)
	e1:SetCost(s.ritcost)
	e1:SetTarget(s.rittg)
	e1:SetOperation(s.ritop)
	c:RegisterEffect(e1)

	-- 2) Ao ser Invocado por Ritual: tributa Ritual Universo G do Deck e Invoca (HOPT)
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCode(EVENT_SPSUMMON_SUCCESS)
	e2:SetCountLimit(1,id+200)
	e2:SetCondition(s.ritcon2)
	e2:SetTarget(s.rittg2)
	e2:SetOperation(s.ritop2)
	c:RegisterEffect(e2)

	-- 3) Substituição de destruição / banimento / envio ao GY (HOPT)
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
	e3:SetCode(EFFECT_DESTROY_REPLACE)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCountLimit(1,id+400)
	e3:SetTarget(s.reptg)
	e3:SetValue(s.repval)
	e3:SetOperation(s.repop)
	c:RegisterEffect(e3)

	local e3b=e3:Clone()
	e3b:SetCode(EFFECT_REMOVE_REPLACE)
	c:RegisterEffect(e3b)

	local e3c=e3:Clone()
	e3c:SetCode(EFFECT_SEND_REPLACE)
	c:RegisterEffect(e3c)

	-- 4) Do GY: banir FD → adicionar Ritual Universo G (Quick, HOPT)
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,2))
	e4:SetType(EFFECT_TYPE_QUICK_O)
	e4:SetCode(EVENT_FREE_CHAIN)
	e4:SetRange(LOCATION_GRAVE)
	e4:SetCountLimit(1,id+600)
	e4:SetCost(s.thcost)
	e4:SetTarget(s.thtg)
	e4:SetOperation(s.thop)
	c:RegisterEffect(e4)
end

-- Efeito 1 — Ritual da mão escavando
function s.ritcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetFieldGroupCount(1-tp,LOCATION_DECK,0)>=2
			and e:GetHandler():IsReleasable()
	end
	Duel.ConfirmDecktop(1-tp,2)
	local g=Duel.GetDecktopGroup(1-tp,2)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_REMOVE)
	local sg=g:Select(tp,1,1,nil)
	sg:GetFirst():SetStatus(STATUS_BANISHED,true)
	e:SetLabelObject(sg:GetFirst())
end

function s.rittg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and e:GetHandler():IsCanBeSpecialSummoned(e,SUMMON_TYPE_RITUAL,tp,false,true)
	end
end

function s.ritop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local tc=e:GetLabelObject()

	-- Banir o card selecionado (se ainda estiver no Deck)
	if tc and tc:IsLocation(LOCATION_DECK) then
		Duel.Remove(tc,POS_FACEUP,REASON_EFFECT)
	end

	if not c:IsRelateToEffect(e) then return end

	-- Tributo correto como Ritual
	Duel.Release(c,REASON_EFFECT+REASON_MATERIAL+REASON_RITUAL)

	-- Ritual Summon real
	Duel.SpecialSummon(c,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP)
	c:CompleteProcedure()
end

-- Efeito 2 — Ritual ao ser Ritual Summoned
function s.ritcon2(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsSummonType(SUMMON_TYPE_RITUAL)
end

function s.ritfilter2(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_RITUAL)
		and c:IsLevelBelow(8)
end

function s.rittg2(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and Duel.IsExistingMatchingCard(s.ritfilter2,tp,LOCATION_DECK,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_DECK)
end

function s.ritop2(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local g=Duel.SelectMatchingCard(tp,s.ritfilter2,tp,LOCATION_DECK,0,1,1,nil)
	local tc=g:GetFirst()
	if not tc then return end

	-- Envia como material de Ritual (NÃO Release)
	Duel.SendtoGrave(tc,REASON_EFFECT+REASON_MATERIAL+REASON_RITUAL)

	-- Ritual Summon correto
	Duel.SpecialSummon(tc,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP)
	tc:CompleteProcedure()
end

-- Efeito 3 — Substituição de remoção
function s.repfilter(c,tp)
	return c:IsControler(tp)
		and c:IsOnField()
		and c:IsReason(REASON_EFFECT)
end

function s.reptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return re
			and re:IsActiveType(TYPE_SPELL+TYPE_TRAP+TYPE_MONSTER)
			and re:GetHandlerPlayer()==1-tp
			and eg:IsExists(s.repfilter,1,nil,tp)
	end
	return Duel.SelectYesNo(tp,aux.Stringid(id,2))
end

function s.repval(e,c)
	return s.repfilter(c,e:GetHandlerPlayer())
end

function s.repop(e,tp,eg,ep,ev,re,r,rp)
	-- apenas substitui
end

-- Efeito 4 — GY → Banir FD + Buscar Ritual
function s.thcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsAbleToRemoveAsCost(POS_FACEDOWN) end
	Duel.Remove(e:GetHandler(),POS_FACEDOWN,REASON_COST)
end

function s.thfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_RITUAL)
		and c:IsAbleToHand()
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.IsExistingMatchingCard(
			s.thfilter,
			tp,
			LOCATION_GRAVE+LOCATION_EXTRA,
			0,
			1,
			c -- EXCLUI este card
		)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_GRAVE+LOCATION_EXTRA)
end

function s.thop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_GRAVE+LOCATION_EXTRA,0,1,1,nil)
	local tc=g:GetFirst()
	if tc then
		Duel.SendtoHand(tc,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,tc)
	end
end