--Mangueira Boy
local s,id=GetID()
function s.initial_effect(c)

	-- 1) Special Summon da mão ou Cemitério
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND+LOCATION_GRAVE)
	e1:SetCountLimit(1,id)
	e1:SetCost(s.spcost)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)

	-- 2) Pode ser tratado como Não-Regulador para Invocação-Sincro
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_NONTUNER)
	e2:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
	e2:SetRange(LOCATION_MZONE)
	e2:SetCondition(s.ntcon)
	c:RegisterEffect(e2)

	-- 3) Mudar Nível para 4
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,2))
	e3:SetType(EFFECT_TYPE_IGNITION)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCountLimit(1,id+200)
	e3:SetOperation(s.lvop)
	c:RegisterEffect(e3)

	-- 4) Escavar 3 e adicionar 1 "Universo G"
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,3))
	e4:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e4:SetType(EFFECT_TYPE_IGNITION)
	e4:SetRange(LOCATION_MZONE)
	e4:SetCountLimit(1,id+400)
	e4:SetTarget(s.thtg)
	e4:SetOperation(s.thop)
	c:RegisterEffect(e4)

	-- 5) Se banido: reciclar e comprar
	local e5=Effect.CreateEffect(c)
	e5:SetDescription(aux.Stringid(id,3))
	e5:SetCategory(CATEGORY_TODECK+CATEGORY_DRAW)
	e5:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e5:SetCode(EVENT_REMOVE)
	e5:SetProperty(EFFECT_FLAG_DELAY)
	e5:SetCountLimit(1,id+600)
	e5:SetTarget(s.rettg)
	e5:SetOperation(s.retop)
	c:RegisterEffect(e5)
end

-- 1) SPECIAL SUMMON
function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		if Duel.GetFieldGroupCount(tp,LOCATION_MZONE,0)==0 then
			return true
		else
			return Duel.CheckLPCost(tp,500)
		end
	end

	if Duel.GetFieldGroupCount(tp,LOCATION_MZONE,0)>0 then
		Duel.PayLPCost(tp,500)
	else
		if Duel.CheckLPCost(tp,500) and Duel.SelectYesNo(tp,aux.Stringid(id,4)) then
			Duel.PayLPCost(tp,500)
		end
	end
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,c,1,0,0)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
end

-- 2) Pode ser Não-Regulador se usado como Matéria-Sincro
function s.ntcon(e)
	return e:GetHandler():IsLocation(LOCATION_MZONE)
end

-- 3) Mudar Nível para 4
function s.lvop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local lv=4
	if c:IsFaceup() and c:IsRelateToEffect(e) then
		-- Set level to announced value (replace current level)
		local cur=c:GetLevel()
		local e1=Effect.CreateEffect(c)
		e1:SetType(EFFECT_TYPE_SINGLE)
		e1:SetCode(EFFECT_UPDATE_LEVEL)
		e1:SetValue(lv - cur)
		e1:SetReset(RESET_EVENT+RESETS_STANDARD)
		c:RegisterEffect(e1)
	end
end

-- 4) Escavar 3
function s.thfilter(c)
	return c:IsSetCard(0xc50) and c:IsAbleToHand()
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then 
		return Duel.GetFieldGroupCount(tp,LOCATION_DECK,0)>=3
	end
end

function s.thop(e,tp,eg,ep,ev,re,r,rp)
	local g=Duel.GetDecktopGroup(tp,3)
	if #g==0 then return end
	Duel.ConfirmCards(tp,g)

	local sg=g:Filter(s.thfilter,nil)
	if #sg>0 then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
		local tg=sg:Select(tp,1,1,nil)
		Duel.SendtoHand(tg,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,tg)
	end

	-- Apenas fechar a revelação
	Duel.ShuffleHand(tp)
end

-- 5) Se banido: reciclar + comprar
function s.retfilter(c)
	return c:IsAbleToDeck()
end

function s.rettg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.retfilter,tp,LOCATION_REMOVED,LOCATION_REMOVED,1,e:GetHandler())
	end
	Duel.SetOperationInfo(0,CATEGORY_TODECK,nil,1,0,LOCATION_REMOVED)
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end

function s.retop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local g=Duel.SelectMatchingCard(tp,s.retfilter,tp,LOCATION_REMOVED,LOCATION_REMOVED,1,1,e:GetHandler())
	if #g>0 then
		if Duel.SendtoDeck(g,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)>0 then
			Duel.Draw(tp,1,REASON_EFFECT)
		end
	end
end
