--Ursos Grandes, Peludos e Mansos!
local s,id=GetID()
function s.initial_effect(c)
	-- Activate
	local e1=Effect.CreateEffect(c)
	e1:SetDescription(aux.Stringid(id,0))
	e1:SetCategory(CATEGORY_SPECIAL_SUMMON+CATEGORY_FUSION_SUMMON+CATEGORY_TODECK)
	e1:SetType(EFFECT_TYPE_ACTIVATE)
	e1:SetCode(EVENT_FREE_CHAIN)
	e1:SetCost(s.cost)
	e1:SetTarget(s.target)
	e1:SetOperation(s.operation)
	c:RegisterEffect(e1)

	-- Hand Quick-Play condition (activate from hand if opponent targeted your monster)
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD)
	e2:SetCode(EFFECT_QP_ACT_IN_NTPHAND)
	e2:SetRange(LOCATION_HAND)
	e2:SetProperty(EFFECT_FLAG_SET_AVAILABLE)
	e2:SetCondition(s.handcon)
	c:RegisterEffect(e2)
end

-----------------------------------------
-- COST: Tribute 1 card you control (except this card)
-----------------------------------------
function s.cfilter(c)
	return c:IsReleasable() and c:IsFaceup() -- you might relax faceup if you allow set cards
end

function s.cost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return Duel.CheckReleaseGroup(tp,s.cfilter,1,nil)
	end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_RELEASE)
	local g=Duel.SelectReleaseGroup(tp,s.cfilter,1,1,nil)
	Duel.Release(g,REASON_COST)
end

-----------------------------------------
-- HAND ACTIVATION CONDITION
-- "You can activate this card from your hand
-- if your opponent targets a monster you control."
-----------------------------------------
function s.handcon(e)
	local tp=e:GetHandlerPlayer()
	local te=Duel.GetChainInfo(0,CHAININFO_TRIGGERING_EFFECT)
	if not te then return false end
	local tg=Duel.GetChainInfo(0,CHAININFO_TARGET_CARDS)
	return tg and tg:IsExists(Card.IsControler,1,nil,tp)
end

-----------------------------------------
-- TARGET (always possible, final checks in operation)
-----------------------------------------
function s.target(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return true end
	Duel.SetOperationInfo(0,CATEGORY_SPECIAL_SUMMON,nil,1,tp,LOCATION_EXTRA+LOCATION_DECK)
end

-----------------------------------------
-- Helpers: universal material pool
-- materials allowed: hand, field, grave (matching earlier discussion)
-----------------------------------------
function s.matpool(tp)
	return Duel.GetMatchingGroup(function(c) return c:IsSetCard(0xc50) end, tp,
		LOCATION_HAND+LOCATION_MZONE+LOCATION_GRAVE, 0, nil)
end

-----------------------------------------
-- OPERATION: choose summon type and validate materials properly
-----------------------------------------
function s.operation(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()
	local opts={ aux.Stringid(id,1), aux.Stringid(id,2), aux.Stringid(id,3), aux.Stringid(id,4), aux.Stringid(id,5) }
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_EFFECT)
	local op=Duel.SelectOption(tp, table.unpack(opts) ) + 1

	if op==1 then
		s.fusion_summon(e,tp)
	elseif op==2 then
		s.synchro_summon(e,tp)
	elseif op==3 then
		s.link_summon(e,tp)
	elseif op==4 then
		s.ritual_summon(e,tp)
	elseif op==5 then
		s.xyz_summon(e,tp)
	end
end

-----------------------------------------
-- 1) FUSÃO: usa motor nativo de Fusion
-- materiais válidos = Duel.GetFusionMaterial(tp)
-----------------------------------------
function s.fusion_summon(e,tp)
	local mg=Duel.GetFusionMaterial(tp):Filter(Card.IsSetCard,nil,0xc50)
	-- busca Fusion Universo G no Extra
	local fg=Duel.GetMatchingGroup(function(c) return c:IsSetCard(0xc50) and c:IsType(TYPE_FUSION) and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_FUSION,tp,false,true) end,
		tp,LOCATION_EXTRA,0,nil)
	if fg:GetCount()==0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local fc=fg:Select(tp,1,1,nil):GetFirst()
	-- solicita ao motor selecionar materiais válidos para essa Fusion
	local mat=nil
	if mg:GetCount()>0 then
		mat=Duel.SelectFusionMaterial(tp,fc,mg)
	end
	if not mat or #mat==0 then return end
	-- envia materiais ao deck e faz Fusion Summon
	Duel.SendtoDeck(mat,nil,SEQ_DECKSHUFFLE,REASON_EFFECT+REASON_MATERIAL+REASON_FUSION)
	Duel.BreakEffect()
	Duel.SpecialSummon(fc,SUMMON_TYPE_FUSION,tp,tp,false,true,POS_FACEUP)
	fc:CompleteProcedure()
end

-----------------------------------------
-- 2) SINCRO: exige 1+ Tuners + non-tuners; verifica soma de níveis
-- materiais permitidos da pool: mão/campo/cemitério (Universo G)
-----------------------------------------
function s.synchro_summon(e,tp)
	local mg=s.matpool(tp)
	if mg:GetCount()==0 then return end
	local sg=Duel.GetMatchingGroup(function(c) return c:IsSetCard(0xc50) and c:IsType(TYPE_SYNCHRO) and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_SYNCHRO,tp,false,true) end,
		tp,LOCATION_EXTRA,0,nil)
	if sg:GetCount()==0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local sc=sg:Select(tp,1,1,nil):GetFirst()
	local lvl=sc:GetLevel()
	-- player selects a group including at least one Tuner; we validate level sum
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SMATERIAL)
	local sel=mg:Select(tp,1,99,nil)
	if #sel==0 then return end
	-- require at least one tuner
	if not sel:IsExists(Card.IsType,1,nil,TYPE_TUNER) then
		Duel.Hint(HINT_MESSAGE,tp,aux.Stringid(id,10) or "Requires at least 1 Tuner")
		return
	end
	-- sum levels
	local sum=0
	for tc in aux.Next(sel) do sum = sum + tc:GetLevel() end
	if sum~=lvl then
		Duel.Hint(HINT_MESSAGE,tp,aux.Stringid(id,11) or "Selected materials levels do not match")
		return
	end
	-- send materials back to deck
	Duel.SendtoDeck(sel,nil,SEQ_DECKSHUFFLE,REASON_EFFECT+REASON_MATERIAL+REASON_SYNCHRO)
	Duel.BreakEffect()
	Duel.SpecialSummon(sc,SUMMON_TYPE_SYNCHRO,tp,tp,false,true,POS_FACEUP)
	sc:CompleteProcedure()
end

-----------------------------------------
-- 3) LINK: select exactly link rating materials (all must be Universo G)
-----------------------------------------
function s.link_summon(e,tp)
	local mg=s.matpool(tp)
	if mg:GetCount()==0 then return end
	local lg=Duel.GetMatchingGroup(function(c) return c:IsSetCard(0xc50) and c:IsType(TYPE_LINK) and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_LINK,tp,false,true) end,
		tp,LOCATION_EXTRA,0,nil)
	if lg:GetCount()==0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local lc=lg:Select(tp,1,1,nil):GetFirst()
	local need = lc:GetLink()
	if need<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local mat = mg:Select(tp,need,need,nil)
	if #mat~=need then return end
	Duel.SendtoDeck(mat,nil,SEQ_DECKSHUFFLE,REASON_EFFECT+REASON_MATERIAL+REASON_LINK)
	Duel.BreakEffect()
	Duel.SpecialSummon(lc,SUMMON_TYPE_LINK,tp,tp,false,true,POS_FACEUP)
	lc:CompleteProcedure()
end

-----------------------------------------
-- 4) RITUAL: simplified per your rule — use 1 Universo G monster as material
-----------------------------------------
function s.ritual_summon(e,tp)
	local mg=s.matpool(tp)
	if mg:GetCount()==0 then return end
	local rg=Duel.GetMatchingGroup(function(c) return c:IsSetCard(0xc50) and c:IsType(TYPE_RITUAL) and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_RITUAL,tp,false,true) end,
		tp,LOCATION_HAND+LOCATION_DECK,0,nil)
	if rg:GetCount()==0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local rc=rg:Select(tp,1,1,nil):GetFirst()
	-- select exactly 1 Universo G as material (the simplified rule)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
	local mat=mg:Select(tp,1,1,nil)
	if #mat==0 then return end
	Duel.SendtoDeck(mat,nil,SEQ_DECKSHUFFLE,REASON_EFFECT+REASON_MATERIAL+REASON_RITUAL)
	Duel.BreakEffect()
	Duel.SpecialSummon(rc,SUMMON_TYPE_RITUAL,tp,tp,false,true,POS_FACEUP)
	rc:CompleteProcedure()
end

-----------------------------------------
-- 5) XYZ: choose exactly Rank number of Universo G materials, overlay them
-----------------------------------------
function s.xyz_summon(e,tp)
	local mg=s.matpool(tp)
	if mg:GetCount()==0 then return end
	local xg=Duel.GetMatchingGroup(function(c) return c:IsSetCard(0xc50) and c:IsType(TYPE_XYZ) and c:IsCanBeSpecialSummoned(e,SUMMON_TYPE_XYZ,tp,false,false) end,
		tp,LOCATION_EXTRA,0,nil)
	if xg:GetCount()==0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_SPSUMMON)
	local xc=xg:Select(tp,1,1,nil):GetFirst()
	local need=xc:GetRank()
	if need<=0 then return end
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
	local mat=mg:Select(tp,need,need,nil)
	if #mat~=need then return end
	-- overlay selected materials to the Xyz then summon it
	Duel.Overlay(xc,mat)
	Duel.BreakEffect()
	Duel.SpecialSummon(xc,SUMMON_TYPE_XYZ,tp,tp,false,false,POS_FACEUP)
	xc:CompleteProcedure()
end
