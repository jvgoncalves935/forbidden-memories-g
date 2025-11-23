--Tom Chinês
local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()
	-- Procedimento padrão: Link Summon usando 1+ monstros
	aux.AddLinkProcedure(c, nil, 1, 99, nil)

	-- Special Summon da mão/Extra Deck como Link Summon sem materiais
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,2))
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e1:SetRange(LOCATION_HAND+LOCATION_EXTRA)
	e1:SetCondition(s.lkcon)
	e1:SetTarget(s.lktg)
	e1:SetOperation(s.lkop)
	c:RegisterEffect(e1)

	-- Restrição: se este card foi Invocado por Invocação-Especial,
	-- você não pode Invocar do Extra Deck exceto “Universo G”
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_CONTINUOUS)
	e2:SetCode(EVENT_SPSUMMON_SUCCESS)
	e2:SetOperation(s.limop)
	c:RegisterEffect(e2)

	-- ESTE MONSTRO NÃO PODE REALIZAR ATAQUES
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_SINGLE)
	e3:SetCode(EFFECT_CANNOT_ATTACK)
	c:RegisterEffect(e3)

	-- Draw 1 card (OBRIGATÓRIO, SOFT OPT)
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,3))
	e4:SetCategory(CATEGORY_DRAW)
	e4:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_TRIGGER_F)
	e4:SetCode(EVENT_LEAVE_FIELD)
	e4:SetRange(LOCATION_MZONE)
	e4:SetProperty(EFFECT_FLAG_DELAY)
	e4:SetCountLimit(1,id)	 -- soft OPT
	e4:SetCondition(s.drcon)
	e4:SetTarget(s.drtg)
	e4:SetOperation(s.drop)
	c:RegisterEffect(e4)
end

--  Special Summon sem materiais
function s.lkcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()

	if Duel.GetFlagEffect(tp,id)~=0 then return false end

	return Duel.GetLocationCountFromEx(tp,tp,nil,c)>0
		or Duel.GetLocationCount(tp,LOCATION_MZONE)>0
end

function s.lktg(e,tp,eg,ep,ev,re,r,rp,c)
	return true
end

function s.lkop(e,tp,eg,ep,ev,re,r,rp,c)
	Duel.RegisterFlagEffect(tp,id,RESET_PHASE+PHASE_END,0,1)
	c:SetMaterial(nil)
end

-- Restrição após Special Summon (Extra Deck lock)
function s.limop(e,tp,eg,ep,ev,re,r,rp)
	local e1=Effect.CreateEffect(e:GetHandler())
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e1:SetTargetRange(1,0)
	e1:SetTarget(function(e,c)
		return c:IsLocation(LOCATION_EXTRA) and not c:IsSetCard(0xc50)
	end)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)
end


-- Ativa quando QUALQUER card seu é movido do campo por efeito do oponente
function s.drcon(e,tp,eg,ep,ev,re,r,rp)
	-- tem que ter sido por efeito do oponente
	if not re or rp==tp then return false end

	-- check nos cards que saíram do campo
	local tc=eg:GetFirst()
	while tc do
		if tc:IsPreviousControler(tp) and tc:IsPreviousLocation(LOCATION_ONFIELD) then
			return true
		end
		tc=eg:GetNext()
	end

	return false
end

-- TARGET: comprar 1
function s.drtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsPlayerCanDraw(tp,1) end
	Duel.SetOperationInfo(0,CATEGORY_DRAW,nil,0,tp,1)
end

-- OPERATION: comprar 1
function s.drop(e,tp,eg,ep,ev,re,r,rp)
	Duel.Draw(tp,1,REASON_EFFECT)
end
