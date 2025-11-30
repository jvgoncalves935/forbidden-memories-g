--Ricco Puentes, The King Of Gueis
local s,id=GetID()

function s.initial_effect(c)
	c:EnableReviveLimit()
	c:SetUniqueOnField(1,0,id)

	-- Xyz Summon padrão
	aux.AddXyzProcedureLevelFree(c, s.mfilter, nil, 2, 2)

	---------------------------------------------
	-- Special Summon alternative (Contact-style)
	---------------------------------------------
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_TOHAND+CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_IGNITION)
	e1:SetRange(LOCATION_EXTRA)
	e1:SetCountLimit(1,id)
	e1:SetCondition(s.spcon)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)
end

-- Material filter
function s.mfilter(c,xyzc)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_NORMAL)
end

---------------------------------------------
-- Condition: checa zonas
---------------------------------------------
function s.spcon(e,tp,eg,ep,ev,re,r,rp)
	return Duel.GetLocationCountFromEx(tp,tp,nil,TYPE_XYZ)>0
end

---------------------------------------------
-- Card que pode ser retornado
---------------------------------------------
function s.cfilter(c)
	return c:IsSetCard(0xc50) and c:IsType(TYPE_NORMAL) and c:IsAbleToHand()
end

---------------------------------------------
-- Target: agora exige **2** monstros
---------------------------------------------
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.cfilter,tp,
			LOCATION_MZONE+LOCATION_GRAVE+LOCATION_REMOVED,0,2,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,2,tp,
		LOCATION_MZONE+LOCATION_GRAVE+LOCATION_REMOVED)
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,e:GetHandler(),1,tp,LOCATION_EXTRA)
end

---------------------------------------------
-- Operation
-- Agora seleciona exatamente **2** monstros
---------------------------------------------
function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if not c:IsRelateToEffect(e) then return end
	if Duel.GetLocationCountFromEx(tp,tp,nil,TYPE_XYZ)<=0 then return end

	-- Seleciona os 2 monstros
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RTOHAND)
	local g=Duel.SelectMatchingCard(tp,s.cfilter,tp,
		LOCATION_MZONE+LOCATION_GRAVE+LOCATION_REMOVED,0,2,2,nil)
	if #g<2 then return end

	-- Retorna à mão
	if Duel.SendtoHand(g,nil,REASON_EFFECT)==0 then return end
	Duel.ConfirmCards(1-tp,g)

	-- Invoca Ricco
	if Duel.SpecialSummon(c,SUMMON_TYPE_SPECIAL,tp,tp,false,false,POS_FACEUP)~=0 then
		c:CompleteProcedure()
	end

	-- aplica restrição até o fim do duelo
	s.register_summon_ban(c,tp)
end

---------------------------------------------
-- Restrição permanente
---------------------------------------------
function s.register_summon_ban(c,p)
	if Duel.GetFlagEffect(p,id+1000)~=0 then return end
	Duel.RegisterFlagEffect(p,id+1000,0,0,0)

	-- cannot Normal Summon
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_CANNOT_SUMMON)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e1:SetTargetRange(1,0)
	e1:SetTarget(s.splimit_all)
	Duel.RegisterEffect(e1,p)

	-- cannot Special Summon
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e2:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e2:SetTargetRange(1,0)
	e2:SetTarget(s.splimit_all)
	Duel.RegisterEffect(e2,p)

	-- cannot Flip Summon
	local e3=Effect.CreateEffect(c)
	e3:SetType(EFFECT_TYPE_FIELD)
	e3:SetCode(EFFECT_CANNOT_FLIP_SUMMON)
	e3:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e3:SetTargetRange(1,0)
	e3:SetTarget(s.splimit_all)
	Duel.RegisterEffect(e3,p)
end

-- Bloqueia invocações de não-Universo G
function s.splimit_all(e,c,sump,sumtype,sumpos,targetp,se)
	return not c:IsSetCard(0xc50)
end
