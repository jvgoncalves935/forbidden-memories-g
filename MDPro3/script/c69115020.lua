--Kid Bengala, O Grande
--c69115020
local s,id=GetID()
function s.initial_effect(c)
	--Permite ser usado como monstro Pêndulo
	aux.EnablePendulumAttribute(c)

	-- Se Invocado por Ritual: buscar Universo G com 2000+ DEF
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOHAND+CATEGORY_SEARCH)
	e1:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e1:SetProperty(EFFECT_FLAG_DELAY)
	e1:SetCode(EVENT_SPSUMMON_SUCCESS)
	e1:SetCountLimit(1,id)
	e1:SetCondition(s.thcon)
	e1:SetTarget(s.thtg)
	e1:SetOperation(s.thop)
	c:RegisterEffect(e1)

	-- Efeito 2: Ritual da mão
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e2:SetType(EFFECT_TYPE_QUICK_O)
	e2:SetRange(LOCATION_HAND)
	e2:SetCode(EVENT_FREE_CHAIN)
	e2:SetCountLimit(1,id+200)
	e2:SetCost(s.ritualcost)
	e2:SetTarget(s.ritualtg)
	e2:SetOperation(s.ritualop)
	c:RegisterEffect(e2)

	--Efeito 3: Efeito Rápido do campo para Zona de Pêndulo
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,2))
	e3:SetCategory(CATEGORY_DESTROY)
	e3:SetType(EFFECT_TYPE_QUICK_O)
	e3:SetRange(LOCATION_MZONE)
	e3:SetCode(EVENT_FREE_CHAIN)
	e3:SetCountLimit(1,id+400)
	e3:SetTarget(s.moveptg)
	e3:SetOperation(s.movepop)
	c:RegisterEffect(e3)

	-- Perfuração
	local e4=Effect.CreateEffect(c)
	e4:SetType(EFFECT_TYPE_SINGLE)
	e4:SetCode(EFFECT_PIERCE)
	c:RegisterEffect(e4)

	-- Dobrar dano perfurante
	local e5=Effect.CreateEffect(c)
	e5:SetType(EFFECT_TYPE_SINGLE)
	e5:SetCode(EFFECT_CHANGE_BATTLE_DAMAGE)
	e5:SetCondition(s.damcon)
	e5:SetValue(aux.ChangeBattleDamage(1,DOUBLE_DAMAGE))
	c:RegisterEffect(e5)

	local e6=Effect.CreateEffect(c)
	e6:SetType(EFFECT_TYPE_SINGLE)
	e6:SetCode(EFFECT_INDESTRUCTABLE_BATTLE)
	e6:SetValue(s.indval)
	c:RegisterEffect(e6)

	local e7=Effect.CreateEffect(c)
	e7:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
	e7:SetCode(EVENT_BATTLE_DAMAGE)
	e7:SetRange(LOCATION_MZONE)
	e7:SetOperation(s.refop)
	c:RegisterEffect(e7)

	-- Pendulum: Ritual/Pendulum Universo G ganham perfuração
	local e8=Effect.CreateEffect(c)
	e8:SetType(EFFECT_TYPE_FIELD)
	e8:SetCode(EFFECT_PIERCE)
	e8:SetRange(LOCATION_PZONE)
	e8:SetTargetRange(LOCATION_MZONE,0)
	e8:SetTarget(s.pentg)
	c:RegisterEffect(e8)

end

function s.thcon(e,tp,eg,ep,ev,re,r,rp)
	return e:GetHandler():IsSummonType(SUMMON_TYPE_RITUAL)
end

function s.thfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_MONSTER)
		and c:IsDefenseAbove(2000)
		and c:IsAbleToHand()
end

function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK,0,1,nil) end
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

function s.ritualcost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then return c:IsReleasable() end
	Duel.Release(c,REASON_COST+REASON_MATERIAL+REASON_RITUAL)
end

-- [Efeito 2] – Ritual da mão
function s.ritualtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,0,0)
end

function s.ritualop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	if not c:IsLocation(LOCATION_GRAVE) then return end

	Duel.SpecialSummon(c,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP)
	c:CompleteProcedure()
end

-- [Efeito 3] – Mover para Zona de Pêndulo
function s.moveptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.CheckLocation(tp,LOCATION_PZONE,0)
			or Duel.CheckLocation(tp,LOCATION_PZONE,1)
			or Duel.IsExistingMatchingCard(Card.IsDestructable,tp,LOCATION_PZONE,0,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,nil,1,tp,LOCATION_PZONE)
end

function s.movepop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end

	local left = Duel.GetFieldCard(tp,LOCATION_PZONE,0)
	local right = Duel.GetFieldCard(tp,LOCATION_PZONE,1)
	local both_full = left and right

	-- 1) Destruição
	if both_full then
		-- há duas cartas: escolha obrigatória de qual destruir
		local g=Group.FromCards(left,right)
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
		local sg=g:Select(tp,1,1,nil)
		if Duel.Destroy(sg,REASON_EFFECT)==0 then return end
	else
		-- se houver ao menos 1 carta nas PZones, perguntamos se o usuário quer destruir
		local g=Group.CreateGroup()
		if left then g:AddCard(left) end
		if right then g:AddCard(right) end
		if #g>0 then
			if Duel.SelectYesNo(tp,aux.Stringid(id,2)) then
				Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
				local sg=g:Select(tp,1,1,nil)
				if Duel.Destroy(sg,REASON_EFFECT)==0 then return end
			end
		end
	end

	-- 2) Mover para PZone se houver espaço
	local canLeft = Duel.CheckLocation(tp,LOCATION_PZONE,0)
	local canRight = Duel.CheckLocation(tp,LOCATION_PZONE,1)

	if not (canLeft or canRight) then
		-- nenhuma PZone livre: nada a fazer
		return
	end

	-- se existir apenas uma livre, movemos para ela; se ambas livres, perguntamos ao jogador
	if canLeft and not canRight then
		Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
		return
	elseif canRight and not canLeft then
		Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
		return
	else
		-- ambas livres. A engine normalmente colocará em uma PZone livre.
		Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
		return
	end
end

function s.damcon(e)
	local c=e:GetHandler()
	local bc=c:GetBattleTarget()
	return bc and bc:IsDefensePos()
end

function s.indcon(e)
	return e:GetHandler():IsStatus(STATUS_ATTACKING)
end

function s.refop(e,tp,eg,ep,ev,re,r,rp)
	if ep==tp then
		Duel.Damage(1-tp,ev,REASON_EFFECT)
	end
end

function s.pentg(e,c)
	return c:IsSetCard(0xc50)
		and (c:IsType(TYPE_RITUAL) or c:IsType(TYPE_PENDULUM))
end

function s.indval(e,tc)
	local c=e:GetHandler()
	return Duel.GetAttacker()==c
end

function s.penzfilter(c)
	return c:IsDestructable()
end
