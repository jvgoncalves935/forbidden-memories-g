--Pote da Delícia
--c69115020
local s,id=GetID()
function s.initial_effect(c)
	--Compre 3 cards e depois revele ou bana mão
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_DRAW+CATEGORY_REMOVE)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetTarget(s.target)
	e1:SetOperation(s.activate)
	c:RegisterEffect(e1)
end

--Verifica se existe algum card "Universo G" na mão
function s.filter(c)
	return c:IsSetCard(0xc50)
end

--Target: comprando 3 cards
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,3) end
	Duel.SetTargetPlayer(tp)
	Duel.SetTargetParam(3)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,3)
end

--Operation: compre 3 e depois revele ou bana
function s.activate(e,tp,eg,ep,ev,re,r,rp)
	local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
	if Duel.Draw(p,d,REASON_EFFECT)==0 then return end

	Duel.BreakEffect()
	local g=Duel.GetFieldGroup(tp,LOCATION_HAND,0)
	local tg=g:Filter(s.filter,nil)

	if #tg>0 then
		-- Se houver pelo menos 1 card "Universo G" na mão, revele 1
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_CONFIRM)
		local sg=tg:Select(tp,1,1,nil)
		Duel.ConfirmCards(1-tp,sg)
		Duel.ShuffleHand(tp)
	else
		-- Caso contrário, bana todos os cards da mão de face para baixo
		if #g>0 then
			Duel.Remove(g,POS_FACEDOWN,REASON_EFFECT)
		end
	end
end
