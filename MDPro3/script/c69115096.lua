--Ursos Grandes, Peludos e Mansos!
local s,id=GetID()

function s.initial_effect(c)

	-- Activate
	local e1=Effect.CreateEffect(c)
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetCountLimit(1,id)
	e1:SetCost(s.cost)
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)

	-- Pode ativar da mão no turno do oponente
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_SINGLE)
	e2:SetCode(EFFECT_QP_ACT_IN_NTPHAND)
	e2:SetCondition(s.handcon)
	c:RegisterEffect(e2)

end

function s.cfilter(c)
	return c:IsReleasable()
end

function s.handcon(e)
	local tp=e:GetHandlerPlayer()
	return Duel.GetTurnPlayer()~=tp
		and Duel.GetTurnCount()==1
		and Duel.GetFieldGroupCount(tp,LOCATION_SZONE,0)==0
end

-- Tribute 1 card
function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.IsExistingMatchingCard(s.cfilter,tp,LOCATION_ONFIELD,0,1,e:GetHandler())
	end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
	local g=Duel.SelectMatchingCard(tp,s.cfilter,tp,LOCATION_ONFIELD,0,1,1,e:GetHandler())
	Duel.Release(g,REASON_COST)
end

-- verifica se um monstro do Extra pode ser invocado
function s.exfilter(c,e,tp)

	if not c:IsSetCard(0xc50) then return false end

	if c:IsType(TYPE_FUSION) then
		local mg=Duel.GetFusionMaterial(tp)
		return c:IsType(TYPE_FUSION)
			and c:CheckFusionMaterial(mg,nil,tp)

	elseif c:IsType(TYPE_SYNCHRO) then
		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
		return c:IsSynchroSummonable(nil,mg)

	elseif c:IsType(TYPE_XYZ) then
		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
		return c:IsXyzSummonable(nil,mg)

	elseif c:IsType(TYPE_LINK) then
		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)
		return c:IsLinkSummonable(nil,mg)

	end

	return false
end

function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)

	if chk==0 then
		return Duel.IsExistingMatchingCard(s.exfilter,tp,LOCATION_EXTRA,0,1,nil,e,tp)
	end

	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)

end

function s.exgfilter(c,mg,mc)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_XYZ)
		and Duel.GetLocationCountFromEx(mc:GetControler(),mc:GetControler(),mg,c)>0
		and mg:CheckSubGroup(s.exgselect,1,#mg,c,mc)
end

function s.exgselect(g,exc,mc)
	return exc:IsXyzSummonable(g,#g,#g)
end

function s.spop(e,tp,eg,ep,ev,re,r,rp)

	local exg=Duel.GetMatchingGroup(s.exfilter,tp,LOCATION_EXTRA,0,nil,e,tp)
	if #exg==0 then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sc=exg:Select(tp,1,1,nil):GetFirst()
	if not sc then return end

	local mat=nil

	-- FUSION
	if sc:IsType(TYPE_FUSION) then

		local mg=Duel.GetFusionMaterial(tp)
		mat=Duel.SelectFusionMaterial(tp,sc,mg,nil,tp)

		sc:SetMaterial(mat)

		local g1=mat:Filter(Card.IsLocation,nil,LOCATION_GRAVE)
		local g2=mat:Filter(Card.IsLocation,nil,LOCATION_HAND+LOCATION_MZONE)

		if #g1>0 then
			Duel.SendtoDeck(g1,nil,SEQ_DECKSHUFFLE,REASON_MATERIAL+REASON_FUSION)
		end
		if #g2>0 then
			Duel.SendtoGrave(g2,REASON_MATERIAL+REASON_FUSION)
		end

		Duel.SpecialSummon(sc,SUMMON_TYPE_FUSION,tp,tp,false,false,POS_FACEUP)

	-- SYNCHRO
	elseif sc:IsType(TYPE_SYNCHRO) then

		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SMATERIAL)
		mat=mg:SelectSubGroup(tp,function(g)
			return sc:IsSynchroSummonable(nil,g)
		end,false,1,sc:GetLevel()+1)

		if not mat then return end

		sc:SetMaterial(mat)
		Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_SYNCHRO)

		Duel.SpecialSummon(sc,SUMMON_TYPE_SYNCHRO,tp,tp,false,false,POS_FACEUP)

	-- XYZ
	elseif sc:IsType(TYPE_XYZ) then

		local c=e:GetHandler()

		if c:IsControler(1-tp) or not c:IsRelateToEffect(e) or c:IsFacedown() then return end

		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
		mat=mg:SelectSubGroup(tp,s.exgselect,false,1,#mg,sc,c)

		sc:SetMaterial(mat)
		Duel.Overlay(sc,mat)

		Duel.SpecialSummon(sc,SUMMON_TYPE_XYZ,tp,tp,false,false,POS_FACEUP)

	-- LINK
	elseif sc:IsType(TYPE_LINK) then

		local mg=Duel.GetMatchingGroup(Card.IsFaceup,tp,LOCATION_MZONE,0,nil)

		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_LMATERIAL)
		mat=mg:SelectSubGroup(tp,function(g)
			return sc:IsLinkSummonable(g)
		end,false,1,sc:GetLink())

		if not mat then return end

		sc:SetMaterial(mat)
		Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_LINK)

		Duel.SpecialSummon(sc,SUMMON_TYPE_LINK,tp,tp,false,false,POS_FACEUP)

	end

	sc:CompleteProcedure()

end