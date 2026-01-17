--Poderoso Castiga
local s,id,o=GetID()
function s.initial_effect(c)
	-- Xyz Summon procedure (manual)
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_SPSUMMON_PROC)
	e1:SetProperty(EFFECT_FLAG_UNCOPYABLE)
	e1:SetRange(LOCATION_EXTRA)
	e1:SetCondition(s.xyzcon)
	e1:SetOperation(s.xyzop)
	c:RegisterEffect(e1)

	-- Battle damage is inflicted to you when this card is attacked in Defense Position
	local e2=Effect.CreateEffect(c)
	e2:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
	e2:SetCode(EVENT_PRE_DAMAGE_CALCULATE)
	e2:SetRange(LOCATION_MZONE)
	e2:SetOperation(s.defdamop)
	c:RegisterEffect(e2)
	
	-- Place 2 Universo G Pendulum Monsters in PZones
	local e4=Effect.CreateEffect(c)
	e4:SetDescription(aux.Stringid(id,2))
	e4:SetType(EFFECT_TYPE_IGNITION)
	e4:SetRange(LOCATION_MZONE)
	e4:SetCountLimit(1,id)
	e4:SetCost(s.pzcost)
	e4:SetTarget(s.pztg)
	e4:SetOperation(s.pzop)
	c:RegisterEffect(e4)

	-- Mandatory negation of monster effects with 2800 or more ATK
	local e5=Effect.CreateEffect(c)
	e5:SetType(EFFECT_TYPE_FIELD+EFFECT_TYPE_CONTINUOUS)
	e5:SetCode(EVENT_CHAINING)
	e5:SetRange(LOCATION_MZONE)
	e5:SetOperation(s.negop)
	c:RegisterEffect(e5)

	-- Bounce 1 monster, then banish this card face-down
	local e6=Effect.CreateEffect(c)
	e6:SetDescription(aux.Stringid(id,3))
	e6:SetType(EFFECT_TYPE_IGNITION)
	e6:SetRange(LOCATION_MZONE)
	e6:SetCountLimit(1) -- soft once per turn
	e6:SetCost(s.bncost)
	e6:SetTarget(s.bntg)
	e6:SetOperation(s.bnoperation)
	c:RegisterEffect(e6)

end

function s.xyzfilter(c)
	return c:IsSetCard(0xc50)
end

function s.xyzcon(e,c)
	if c==nil then return true end
	local tp=c:GetControler()

	-- Máximo de 3 Invocações-Especiais no turno
	if Duel.GetActivityCount(tp,ACTIVITY_SPSUMMON)>3 then
		return false
	end

	-- Precisa de 3 "Universo G" no campo (face-up ou face-down)
	return Duel.GetLocationCount(tp,LOCATION_MZONE)>0
		and Duel.IsExistingMatchingCard(
			s.xyzfilter,tp,LOCATION_ONFIELD,0,1,nil
		)
end

function s.xyzop(e,tp,eg,ep,ev,re,r,rp,c)
	-- Seleciona 3 matérias
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_XMATERIAL)
	local g=Duel.SelectMatchingCard(
		tp,s.xyzfilter,tp,LOCATION_ONFIELD,0,1,1,nil
	)

	c:SetMaterial(g)
	Duel.Overlay(c,g)

	-- Lock de Invocações pelo resto do turno
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_FIELD)
	e1:SetCode(EFFECT_CANNOT_SUMMON)
	e1:SetProperty(EFFECT_FLAG_PLAYER_TARGET)
	e1:SetTargetRange(1,0)
	e1:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e1,tp)

	local e2=e1:Clone()
	e2:SetCode(EFFECT_CANNOT_SPECIAL_SUMMON)
	Duel.RegisterEffect(e2,tp)

	-- Não pode declarar ataques neste turno
	local e3=Effect.CreateEffect(e:GetHandler())
	e3:SetType(EFFECT_TYPE_FIELD)
	e3:SetCode(EFFECT_CANNOT_DIRECT_ATTACK)
	e3:SetTargetRange(LOCATION_MZONE,0)
	e3:SetReset(RESET_PHASE+PHASE_END)
	Duel.RegisterEffect(e3,tp)

end

function s.pzfilter(c)
	return c:IsSetCard(0xc50)
		and c:IsType(TYPE_PENDULUM)
		and c:IsLevelBelow(5)
		and not c:IsForbidden()
end

function s.pzcost(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then return Duel.CheckLPCost(tp,2800) end
	Duel.PayLPCost(tp,2800)
end

function s.pztg(e,tp,eg,ep,ev,re,r,rp,chk)
	if chk==0 then
		return s.check_pzones(tp)
			and Duel.IsExistingMatchingCard(
				s.pzfilter,tp,
				LOCATION_DECK+LOCATION_HAND+LOCATION_GRAVE+LOCATION_REMOVED,
				0,2,nil
			)
	end
end

function s.check_pzones(tp)
	return Duel.GetFieldCard(tp,LOCATION_PZONE,0)==nil
		and Duel.GetFieldCard(tp,LOCATION_PZONE,1)==nil
end


function s.pzop(e,tp,eg,ep,ev,re,r,rp)
	-- Confirma se ambas as zonas estão livres
	if Duel.GetFieldCard(tp,LOCATION_PZONE,0)
		or Duel.GetFieldCard(tp,LOCATION_PZONE,1) then
		return
	end

	-- Seleciona o primeiro monstro (Zona de Pêndulo esquerda)
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOFIELD)
	local g1=Duel.SelectMatchingCard(
		tp,s.pzfilter,tp,
		LOCATION_DECK+LOCATION_EXTRA+LOCATION_GRAVE+LOCATION_REMOVED,
		0,1,1,nil
	)
	if #g1==0 then return end
	local tc1=g1:GetFirst()

	Duel.MoveToField(tc1,tp,tp,LOCATION_PZONE,POS_FACEUP,true)

	-- Seleciona o segundo monstro (Zona de Pêndulo direita), excluindo o primeiro
	Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TOFIELD)
	local g2=Duel.SelectMatchingCard(
		tp,s.pzfilter,tp,
		LOCATION_DECK+LOCATION_EXTRA+LOCATION_GRAVE+LOCATION_REMOVED,
		0,1,1,tc1
	)
	if #g2==0 then return end
	local tc2=g2:GetFirst()

	Duel.MoveToField(tc2,tp,tp,LOCATION_PZONE,POS_FACEUP,true)
end

function s.defdamop(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	-- Este card precisa ser o alvo do ataque
	if Duel.GetAttackTarget()~=c then return end

	-- Precisa estar em posição de defesa
	if not c:IsDefensePos() then return end

	local a=Duel.GetAttacker()
	if not a or not a:IsRelateToBattle() then return end

	local atk=a:GetAttack()
	local def=c:GetDefense()
	if atk<=def then return end

	local dmg=atk-def

	-- Zera qualquer dano de batalha padrão
	Duel.ChangeBattleDamage(tp,0)

	-- Aplica dano manualmente ao controlador deste card
	Duel.Damage(tp,dmg,REASON_BATTLE)
end

function s.negop(e,tp,eg,ep,ev,re,r,rp)
	-- Só se for efeito de monstro
	if not re:IsActiveType(TYPE_MONSTER) then return end

	local rc=re:GetHandler()
	if not rc then return end

	-- ATK 2800 ou mais
	if rc:GetAttack()<2800 then return end

	-- Precisa poder ser negado
	if not Duel.IsChainNegatable(ev) then return end

	Duel.NegateEffect(ev)
end

function s.bncost(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return c:CheckRemoveOverlayCard(tp,1,REASON_COST)
	end
	c:RemoveOverlayCard(tp,1,1,REASON_COST)
end

function s.bnfilter(c,sc)
	return c:IsType(TYPE_MONSTER) and c~=sc
end

function s.bntg(e,tp,eg,ep,ev,re,r,rp,chk)
	local c=e:GetHandler()
	if chk==0 then
		return Duel.IsExistingMatchingCard(
			s.bnfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil,c
		)
	end
end

function s.bnoperation(e,tp,eg,ep,ev,re,r,rp)
	local c=e:GetHandler()

	-- Tenta devolver 1 monstro do campo para o Deck (se existir)
	if Duel.IsExistingMatchingCard(
		s.bnfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,nil,c
	) then
		Duel.Hint(HINT_SELECTMSG,tp,HINTMSG_TODECK)
		local g=Duel.SelectMatchingCard(
			tp,s.bnfilter,tp,LOCATION_MZONE,LOCATION_MZONE,1,1,nil,c
		)
		local tc=g:GetFirst()
		if tc then
			Duel.SendtoDeck(tc,nil,SEQ_DECKSHUFFLE,REASON_EFFECT)
		end
	end

	-- Bane este card de face para baixo (independente do retorno)
	if c:IsRelateToEffect(e) then
		Duel.Remove(c,POS_FACEDOWN,REASON_EFFECT)
	end
end
