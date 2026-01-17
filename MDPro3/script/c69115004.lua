--Índio (Indígena)
local s,id=GetID()
function s.initial_effect(c)
	-- Quick Synchro from hand
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON)
	e1:SetType(EFFECT_TYPE_QUICK_O)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetRange(LOCATION_HAND)
	e1:SetHintTiming(0,TIMINGS_CHECK_MONSTER+TIMING_END_PHASE)
	e1:SetCountLimit(1,id) -- hard once per turn
	e1:SetTarget(s.sptg)
	e1:SetOperation(s.spop)
	c:RegisterEffect(e1)

	-- Set Universo G Spell/Trap if used as material
	local e2=Effect.CreateEffect(c)
	e2:SetDescription(aux.Stringid(id,1))
	e2:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_O)
	e2:SetProperty(EFFECT_FLAG_DELAY)
	e2:SetCode(EVENT_BE_MATERIAL)
	e2:SetCountLimit(1,id+200) -- hard once per turn separado
	e2:SetCondition(s.matcond)
	e2:SetTarget(s.sttg)
	e2:SetOperation(s.stop)
	c:RegisterEffect(e2)

	-- Burn when leaving the field
	local e3=Effect.CreateEffect(c)
	e3:SetDescription(aux.Stringid(id,2))
	e3:SetCategory(CATEGORY_DAMAGE)
	e3:SetType(EFFECT_TYPE_SINGLE+EFFECT_TYPE_TRIGGER_F)
	e3:SetCode(EVENT_LEAVE_FIELD)
	e3:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e3:SetCountLimit(1,id+300) -- hard once per turn
	e3:SetCondition(s.damcon)
	e3:SetTarget(s.damtg)
	e3:SetOperation(s.damop)
	c:RegisterEffect(e3)

end

-- Deck material filter (Universo G monster)
function s.matfilter(c,needlv)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_MONSTER)
		and c:GetLevel()==needlv
end

function s.validscfilter(c,e,tp,handc)
	if not (c:IsSetCard(0xc50)
		and c:IsType(TYPE_SYNCHRO)
		and c:IsLevelBelow(6)
		and Duel.GetLocationCountFromEx(tp,tp,nil,c)>0
		and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_SYNCHRO,tp,false,false)) then
		return false
	end

	local needlv=c:GetLevel()-handc:GetLevel()
	if needlv<=0 then return false end

	return Duel.IsExistingMatchingCard(
		s.matfilter,tp,LOCATION_DECK,0,1,nil,needlv
	)
end


function s.sptg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return false end
		local sg=Duel.GetMatchingGroup(s.validscfilter,tp,LOCATION_EXTRA,0,nil,e,tp,c)
		return sg:IsExists(function(sc)
			local needlv=sc:GetLevel()-c:GetLevel()
			return needlv>0 and Duel.IsExistingMatchingCard(
				s.matfilter,tp,LOCATION_DECK,0,1,nil,needlv)
		end,1,nil)
	end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA)
end


function s.spop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	if Duel.GetLocationCount(tp,LOCATION_MZONE)<=0 then return end
	if not c:IsRelateToEffect(e) then return end

	-- escolhe o Sincro primeiro
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sc=Duel.SelectMatchingCard(tp,s.validscfilter,tp,LOCATION_EXTRA,0,1,1,nil,e,tp,c):GetFirst()
	if not sc then return end

	local needlv=sc:GetLevel()-c:GetLevel()
	if needlv<=0 then return end

	-- escolhe o material correto do Deck
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SMATERIAL)
	local mg=Duel.SelectMatchingCard(tp,s.matfilter,tp,LOCATION_DECK,0,1,1,nil,needlv)
	local mc=mg:GetFirst()
	if not mc then return end

	-- envia materiais (ORDEM CORRETA)
	local mat=Group.FromCards(c,mc)

	-- registra as matérias antes do envio
	sc:SetMaterial(mat)

	-- agora envia corretamente como matéria Sincro
	Duel.SendtoGrave(mat,REASON_MATERIAL+REASON_SYNCHRO)

	-- invocação sincro manual
	if Duel.SpecialSummon(sc,SUMMON_TYPE_SYNCHRO,tp,tp,false,false,POS_FACEUP)>0 then
		sc:CompleteProcedure()
	end

	-- Synchro Summon lock for the rest of the turn (engine-safe)
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET+EFFECT_FLAG_OATH)
	e1:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	e1:SetTargetRange(1,0)
	e1:SetTarget(s.synclimit)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)

end

function s.synclimit(e,c,tp,sumtp,sumpos)
	return bit.band(sumtp,SUMMON_TYPE_SYNCHRO)==SUMMON_TYPE_SYNCHRO
end

function s.stfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_SPELL+TYPE_TRAP)
		and c:IsSSetable()
end

function s.matcond(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsReason(REASON_MATERIAL)
		and c:IsReason(REASON_SYNCHRO+REASON_FUSION+REASON_LINK)
end


function s.sttg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.GetLocationCount(tp,LOCATION_SZONE)>0
			and Duel.IsExistingMatchingCard(s.stfilter,tp,LOCATION_DECK,0,1,nil)
	end
end

function s.stop(e,tp,eg,ep,ev,re,r,rp)
	if Duel.GetLocationCount(tp,LOCATION_SZONE)<=0 then return end

	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SET)
	local g=Duel.SelectMatchingCard(tp,s.stfilter,tp,LOCATION_DECK,0,1,1,nil)
	local tc=g:GetFirst()
	if tc then
		Duel.SSet(tp,tc)
	end
end

function s.damcon(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	return c:IsPreviousLocation(LOCATION_ONFIELD)
end

function s.damtg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.SetTargetPlayer(1-tp)
	Duel.SetTargetParam(600)
	Duel.SetOperationInfo(0,CATEGORY_DAMAGE,nil,0,1-tp,600)
end

function s.damop(e,tp,eg,ep,ev,re,r,rp)
	local p,d=Duel.GetChainInfo(0,CHAININFO_TARGET_PLAYER,CHAININFO_TARGET_PARAM)
	Duel.Damage(p,d,REASON_EFFECT)
end
