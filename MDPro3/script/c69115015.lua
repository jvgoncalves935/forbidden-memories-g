-- Maldita Hora Que Eu Sentei Nesse Banco
local s,id=GetID()

function s.initial_effect(c)

	-- Ativar
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetCountLimit(1,id) -- hard once per turn
	e1:SetCondition(s.actcon)
	e1:SetTarget(s.acttg)
	e1:SetOperation(s.actop)
	c:RegisterEffect(e1)

	-- Ativar da mão no turno do oponente se não controla cards
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_QP_ACT_IN_NTPHAND)
	e2:SetCondition(s.handcon)
	c:RegisterEffect(e2)

end

-- Condição para ativar da mão no turno do oponente
function s.handcon(e)
	local tp=e:GetHandlerPlayer()
	return Duel.GetTurnPlayer()~=tp
		and Duel.GetFieldGroupCount(tp,LOCATION_ONFIELD,0)==0
end

-- Condição geral de ativação (evita ativar sem 3 alvos)
function s.actcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,3,nil)
end

function s.thfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_SPELL+TYPE_TRAP)
		and c:IsAbleToHand()
end

function s.acttg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,3,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK)
end

function s.actop(e,tp,eg,ep,ev,re,r,rp)

	-- Parte 1: Reveal 3
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_DECK,0,3,3,nil)

	if #g==3 then
		Duel.ConfirmCards(1-tp,g)

		local sg=g:RandomSelect(1-tp,1)
		local tc=sg:GetFirst()

		Duel.SendtoHand(tc,nil,REASON_EFFECT)
		Duel.ConfirmCards(tp,tc)

		g:RemoveCard(tc)
		Duel.SendtoDeck(g,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
	end

	-- Parte 2: Bounce opcional
	if Duel.IsExistingMatchingCard(s.bouncefilter,tp,LOCATION_ONFIELD,0,1,e:GetHandler()) then
		if Duel.SelectYesNo(tp,aux.Stringid(id,1)) then
			Duel.BreakEffect()

			Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
			local rg=Duel.SelectMatchingCard(tp,s.bouncefilter,tp,LOCATION_ONFIELD,0,1,1,e:GetHandler())
			local rc=rg:GetFirst()

			if rc and Duel.SendtoHand(rc,nil,REASON_EFFECT)>0 then
				Duel.BreakEffect()

				-- só tenta destruir se existir alvo
				local dg=Duel.GetMatchingGroup(s.stzonefilter,tp,0,LOCATION_SZONE,nil)
				if #dg>0 then
					Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
					local sg=dg:Select(tp,1,1,nil)
					Duel.Destroy(sg,REASON_EFFECT)
				end
			end
		end
	end
end


function s.bouncefilter(c)
	return c:IsAbleToHand()
end

function s.stzonefilter(c)
	return c:IsLocation(LOCATION_SZONE)
		and c:IsDestructable()
end
