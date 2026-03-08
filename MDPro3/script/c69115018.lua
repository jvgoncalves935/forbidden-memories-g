--Yeah Man
local s,id=GetID()

function s.initial_effect(c)

	aux.EnablePendulumAttribute(c)

	-- Quick summon from hand
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER)
	e1:SetCountLimit(1,id)
	e1:SetCost(s.spcost)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)

	-- Move to Pendulum Zone
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCode(EVENT_TO_GRAVE)
	e2:SetCountLimit(1,id+100)
	e2:SetCondition(s.pzcon)
	e2:SetTarget(s.pztg)
	e2:SetOperation(s.pzop)
	c:RegisterEffect(e2)

	local e3=e2:Clone()
	e3:SetCode(EVENT_REMOVE)
	c:RegisterEffect(e3)

	local e4=e2:Clone()
	e4:SetCode(EVENT_TO_EXTRA)
	c:RegisterEffect(e4)

	-- Used as material
	local e5=Effect.CreateEffect(c)
	e5:SetDescription(aux.Stringid(id,2))
	e5:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e5:SetProperty(EFFECT_FLAG_DELAY)
	e5:SetCode(EVENT_BE_MATERIAL)
	e5:SetCountLimit(1,id+200)
	e5:SetCondition(s.matcon)
	e5:SetTarget(s.mattg)
	e5:SetOperation(s.matop)
	c:RegisterEffect(e5)

	-- Pendulum ATK boost
	local e6=Effect.CreateEffect(c)
	e6:SetType(EFFECT_TYPE_FIELD)
	e6:SetCode(EFFECT_UPDATE_ATTACK)
	e6:SetRange(LOCATION_PZONE)
	e6:SetTargetRange(LOCATION_MZONE,0)
	e6:SetTarget(s.atktg)
	e6:SetValue(400)
	c:RegisterEffect(e6)

	local e7=e6:Clone()
	e7:SetCode(EFFECT_UPDATE_DEFENSE)
	c:RegisterEffect(e7)

	-- Special from PZone
	local e8=Effect.CreateEffect(c)
	e8:SetDescription(aux.Stringid(id,3))
	e8:SetType(EFFECT_TYPE_QUICK_O)
	e8:SetCode(EVENT_FREE_CHAIN)
	e8:SetRange(LOCATION_PZONE)
	e8:SetCountLimit(1)
	e8:SetTarget(s.pstg)
	e8:SetOperation(s.psop)
	c:RegisterEffect(e8)

end

function s.spcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return e:GetHandler():IsDiscardable() end
	Duel.SendtoGrave(e:GetHandler(),REASON_COST+REASON_DISCARD)
end

function s.spfilter(c,e,tp)
	if not c:IsSetCard(0xc50) then return false end

	if c:IsType(TYPE_FUSION) then
		return Duel.IsExistingMatchingCard(s.fusmat,tp,LOCATION_HAND+LOCATION_MZONE,0,1,nil,c,tp)
	elseif c:IsType(TYPE_SYNCHRO) then
		return Duel.IsExistingMatchingCard(Card.IsFaceup,tp,LOCATION_MZONE,0,1,nil)
	elseif c:IsType(TYPE_XYZ) then
		return Duel.IsExistingMatchingCard(Card.IsFaceup,tp,LOCATION_MZONE,0,2,nil)
	elseif c:IsType(TYPE_LINK) then
		return Duel.IsExistingMatchingCard(Card.IsFaceup,tp,LOCATION_MZONE,0,1,nil)
	end

	return false
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.spfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp)
	end
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local opt=Duel.SelectOption(tp,
		aux.Stringid(id,3), -- Fusion
		aux.Stringid(id,4), -- Synchro
		aux.Stringid(id,5), -- Xyz
		aux.Stringid(id,6)  -- Link
	)

	if opt==0 then
		s.doFusion(e,tp)
	elseif opt==1 then
		s.doSynchro(e,tp)
	elseif opt==2 then
		s.doXyz(e,tp)
	else
		s.doLink(e,tp)
	end
end

function s.fusionfilter(c,e,tp)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_FUSION)
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,false)
end

function s.doFusion(e,tp)

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local fc=Duel.SelectMatchingCard(
		tp,s.fusionfilter,tp,LOCATION_EXTRA,0,1,1,nil,e,tp
	):GetFirst()
	if not fc then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
	local mg1=Duel.SelectMatchingCard(
		tp,Card.IsType,tp,LOCATION_HAND+LOCATION_MZONE,0,1,1,nil,TYPE_MONSTER
	):GetFirst()
	if not mg1 then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_FMATERIAL)
	local mg2=Duel.SelectMatchingCard(
		tp,Card.IsType,tp,LOCATION_HAND+LOCATION_MZONE,0,1,1,nil,TYPE_MONSTER
	):GetFirst()
	if not mg2 then return end

	local mat=Group.FromCards(mg1,mg2)

	if not fc:CheckFusionMaterial(mat,nil,tp) then return end

	fc:SetMaterial(mat)
	Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_FUSION)

	Duel.SpecialSummon(fc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)
	fc:CompleteProcedure()
end

function s.syncfilter(c,e,tp)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_SYNCHRO)
end

function s.doSynchro(e,tp)

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sc=Duel.SelectMatchingCard(
		tp,s.syncfilter,tp,LOCATION_EXTRA,0,1,1,nil,e,tp
	):GetFirst()
	if not sc then return end

	local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SMATERIAL)
	local mat=mg:SelectSubGroup(tp,function(g)
		return sc:IsSynchroSummonable(nil,g)
	end,false,2,2)

	if not mat then return end

	sc:SetMaterial(mat)
	Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_SYNCHRO)

	Duel.SpecialSummon(sc,SUMMON_TYPE_SYNCHRO,tp,tp,false,false,POS_FACEUP)
	sc:CompleteProcedure()
end

function s.exgselect(g,sc)
	if not sc:IsXyzSummonable(g) then return false end
	return not g:IsExists(function(c,sg,sc)
		local g2=sg:Clone()
		g2:RemoveCard(c)
		return sc:IsXyzSummonable(g2)
	end,1,nil,g,sc)
end

function s.xyzfilter(c,mg)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_XYZ)
		and mg:CheckSubGroup(s.exgselect,1,#mg,c)
end

function s.doXyz(e,tp)

	local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

	local exg=Duel.GetMatchingGroup(s.xyzfilter,tp,LOCATION_EXTRA,0,nil,mg)
	if #exg==0 then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sc=exg:Select(tp,1,1,nil):GetFirst()
	if not sc then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
	local mat=mg:SelectSubGroup(tp,s.exgselect,false,1,#mg,sc)
	if not mat then return end

	if Duel.GetLocationCountFromEx(tp,tp,mat,sc)<=0 then return end

	sc:SetMaterial(mat)

	Duel.Overlay(sc,mat)

	Duel.SpecialSummon(sc,SUMMON_TYPE_XYZ,tp,tp,false,false,POS_FACEUP)

	sc:CompleteProcedure()
end

function s.linkfilter(c,mg)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_LINK)
		and c:IsLinkSummonable(mg)
end

function s.doLink(e,tp)

	local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

	local exg=Duel.GetMatchingGroup(s.linkfilter,tp,LOCATION_EXTRA,0,nil,mg)
	if #exg==0 then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sc=exg:Select(tp,1,1,nil):GetFirst()

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_LINK)
	local mat=mg:SelectSubGroup(tp,function(g)
		return sc:IsLinkSummonable(g)
	end,false,1,sc:GetLink())

	if not mat then return end

	if Duel.GetLocationCountFromEx(tp,tp,mat,sc)<=0 then return end

	sc:SetMaterial(mat)
	Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_LINK)

	Duel.SpecialSummon(sc,SUMMON_TYPE_LINK,tp,tp,false,false,POS_FACEUP)
	sc:CompleteProcedure()
end

function s.pzcon(e,tp)
	local c=e:GetHandler()
	return c:IsPreviousLocation(LOCATION_DECK+LOCATION_ONFIELD)
end

function s.pztg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckLocation(tp,LOCATION_PZONE,0)
		or Duel.CheckLocation(tp,LOCATION_PZONE,1)
	end
end

function s.pzop(e,tp)
	local c=e:GetHandler()
	if Duel.CheckLocation(tp,LOCATION_PZONE,0)
		or Duel.CheckLocation(tp,LOCATION_PZONE,1) then
		Duel.MoveToField(c,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
	end
end

function s.matcon(e,tp,eg,ep,ev,re,r,rp)
	return r&(REASON_SYNCHRO+REASON_FUSION+REASON_LINK)~=0
end

function s.atktg(e,c)
	return c:IsSetCard(0xc50)
end

function s.pstg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
			and c:IsCanBeSpecialSummoned(e,0,tp,false,false)
	end
end

function s.psop(e,tp)
	local c=e:GetHandler()
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	Duel.SpecialSummon(c,0,tp,tp,false,false,POS_FACEUP)
end