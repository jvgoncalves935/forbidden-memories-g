--Panty Anarchy
--c69069001
local s,id=GetID()
function s.initial_effect(c)
	c:EnableReviveLimit()

	--Treat this card as mentioning "Toon World"
	aux.AddCodeList(c, 15259703)

	--Special Summon from hand by sending 1 Extra Deck monster to grave
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

	--Direct attack condition (Mundo Toon or Mundo da PUTARIA)
	local e7=Effect.CreateEffect(c)
	e7:SetType(EFFECT_TYPE_SINGLE)
	e7:SetCode(EFFECT_DIRECT_ATTACK)
	e7:SetCondition(s.dircon)
	c:RegisterEffect(e7)

	--Add 1 "Anarchy" monster to hand when Summoned
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

	--Quick effect: destroy 1 card on field (now targets properly any card on either field)
	local e11=Effect.CreateEffect(c)
	e11:SetDescription(aux.Stringid(id,2))
	e11:SetCategory(CATEGORY_DESTROY)
	e11:SetType(EFFECT_TYPE_QUICK_O)
	e11:SetCode(EVENT_FREE_CHAIN)
	e11:SetRange(LOCATION_MZONE)
	e11:SetProperty(EFFECT_FLAG_CARD_TARGET)
	e11:SetCountLimit(1,id+100)
	e11:SetTarget(s.destg2)
	e11:SetOperation(s.desop2)
	c:RegisterEffect(e11)
end

--Special Summon helper
function s.cfilter(c)
	return c:IsAbleToGraveAsCost() and c:IsType(TYPE_MONSTER)
end

function s.spcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()
	return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsExistingMatchingCard(s.cfilter,tp,LOCATION_EXTRA,0,1,nil)
end

-- seleciona 1 monstro do Extra Deck para enviar ao GY como custo
function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk,c)
	if chk==0 then return true end
	local g=Duel.GetMatchingGroup(s.cfilter,tp,LOCATION_EXTRA,0,nil)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOGRAVE)
	-- mantém SelectUnselect conforme solicitado; trata o retorno flexível
	local sel = g:SelectUnselect(nil,tp,false,true,1,1)
	if sel then
		e:SetLabelObject(sel)
		return true
	end
	return false
end

function s.spop(e,tp,eg,ep,ev,re,r,rp,c)
	local obj=e:GetLabelObject()
	if not obj then return end
	-- SelectUnselect pode retornar um Card ou um Group; trate ambos
	if type(obj)=="table" and obj.GetFirst then
		-- é um Group
		Duel.SendtoGrave(obj,REASON_COST+REASON_SPSUMMON)
	else
		-- é um Card
		Duel.SendtoGrave(obj,REASON_COST+REASON_SPSUMMON)
	end
	-- apply global summon ban for rest of duel (passa o card handler para criar efeitos com owner)
	local hc = c or e:GetHandler()
	if not hc then hc = e:GetHandler() end
	s.register_summon_ban(hc,tp)
end

--Direct attack condition
function s.dircon(e)
	local tp=e:GetHandlerPlayer()
	return Duel.IsExistingMatchingCard(function(cc) return cc:IsFaceup() and (cc:IsCode(15259703) or cc:IsCode(69069069)) end, tp, LOCATION_ONFIELD, 0, 1, nil)
end

--Search Anarchy
function s.thfilter(c)
	return c:IsSetCard(0xf6f) and c:IsType(TYPE_MONSTER) and not c:IsCode(id) and c:IsAbleToHand()
end
function s.thtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.IsExistingMatchingCard(s.thfilter,tp,LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,0,1,nil) end
	Duel.SetOperationInfo(0,CATEGORY_TOHAND,nil,1,tp,LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED)
end
function s.thop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_ATOHAND)
	local g=Duel.SelectMatchingCard(tp,s.thfilter,tp,LOCATION_DECK+LOCATION_GRAVE+LOCATION_REMOVED,0,1,1,nil)
	if #g>0 then
		Duel.SendtoHand(g,nil,REASON_EFFECT)
		Duel.ConfirmCards(1-tp,g)
	end
	-- apply global summon ban for rest of duel (use handler c)
	s.register_summon_ban(c,tp)
end

--Quick effect destroy (agora com alvo)
function s.destg2(e,tp,eg,ep,ev,re,r,rp,chk,chkc)
	if chkc then return chkc:IsOnField() end
	if chk==0 then return Duel.IsExistingTarget(aux.TRUE,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,nil) end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_DESTROY)
	local g=Duel.SelectTarget(tp,aux.TRUE,tp,LOCATION_ONFIELD,LOCATION_ONFIELD,1,1,nil)
	Duel.SetOperationInfo(0,CATEGORY_DESTROY,g,1,0,0)
end
function s.desop2(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local tc=Duel.GetFirstTarget()
	if tc and tc:IsRelateToEffect(e) then
		Duel.Destroy(tc,REASON_EFFECT)
	end
	-- apply global summon ban for rest of duel
	s.register_summon_ban(c,tp)
end

-- register global summon-ban for player 'p' for rest of duel
-- agora recebe o card 'c' para criar efeitos corretamente ligados ao card
function s.register_summon_ban(c,p)
	-- check if already applied (prevent stacking)
	if Duel.GetFlagEffect(p,id+1000)~=0 then return end
	Duel.RegisterFlagEffect(p,id+1000,0,0,0)
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
