-- Doutora's Hospital
local s,id=GetID()
function s.initial_effect(c)
	-- Ativação do card
	local e0=Effect.CreateEffect(c)
	e0:SetType(EFFECT_TYPE_ACTIVATE)
	e0:SetCode(EVENT_FREE_CHAIN)
	c:RegisterEffect(e0)
	
	-- Oponente não pode retornar seus cards para a mão
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetRange(LOCATION_SZONE)
	e1:SetCode(EFFECT_CANNOT_TO_HAND)
	e1:SetTargetRange(LOCATION_ONFIELD+LOCATION_GRAVE+LOCATION_REMOVED,0)
	e1:SetTarget(s.retlmit)
	c:RegisterEffect(e1)

	-- Oponente não pode retornar seus cards para o Deck
	local e1b=e1:Clone()
	e1b:SetCode(EFFECT_CANNOT_TO_DECK)
	c:RegisterEffect(e1b)

	-- Efeito rápido
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetCode(EVENT_FREE_CHAIN)
	e2:SetRange(LOCATION_SZONE)
	e2:SetCountLimit(1,id) -- hard once per turn
	e2:SetTarget(s.eftg)
	e2:SetOperation(s.efop)
	c:RegisterEffect(e2)
end

function s.retlmit(e,c)
	-- só bloqueia se o efeito for do oponente
	local re = Duel.GetCurrentChain() > 0 and Duel.GetChainInfo(Duel.GetCurrentChain(),CHAININFO_TRIGGERING_EFFECT) or nil
	if not re then return false end
	return re:GetHandlerPlayer() ~= e:GetHandlerPlayer()
end

function s.ugfilter(c)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_MONSTER)
end

function s.thfilter(c)
	return c:IsSetCard(0xc50) and c:IsAbleToHand()
end

function s.eftg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.ugfilter,tp,LOCATION_MZONE,0,1,nil)
	end
end

function s.efop(e,tp,eg,ep,ev,re,r,rp)

	-- 1) escolher monstro Universo G (sem target)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
	local tc=Duel.SelectMatchingCard(
		tp,s.ugfilter,tp,LOCATION_MZONE,0,1,1,nil
	):GetFirst()
	if not tc then return end

	-- retorna para a mão
	Duel.SendtoHand(tc,nil,REASON_EFFECT)

	Duel.BreakEffect()

	-- 2) opção: enviar do Extra Deck
	if Duel.GetFieldGroupCount(tp,LOCATION_EXTRA,0)>0 then
		if Duel.SelectYesNo(tp,aux.Stringid(id,1)) then
			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
			local g=Duel.SelectMatchingCard(
				tp,Card.IsAbleToGrave,tp,LOCATION_EXTRA,0,1,1,nil
			)
			Duel.SendtoGrave(g,REASON_EFFECT)
			Duel.BreakEffect()
		end
	end

	-- 3) escolher efeito final
	local opt=Duel.SelectOption(
		tp,
		aux.Stringid(id,2), -- adicionar
		aux.Stringid(id,3)  -- destruir
	)

	if opt==0 then
		-- adicionar card Universo G
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
		local g=Duel.SelectMatchingCard(
			tp,s.thfilter,tp,LOCATION_DECK,0,1,1,nil
		)
		if #g>0 then
			Duel.SendtoHand(g,nil,REASON_EFFECT)
			Duel.ConfirmCards(1-tp,g)
		end
	else
		-- destruir card no campo (sem target)
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
		local g=Duel.SelectMatchingCard(
			tp,Card.IsOnField,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,1,nil
		)
		if #g>0 then
			Duel.Destroy(g,REASON_EFFECT)
		end
	end
end

