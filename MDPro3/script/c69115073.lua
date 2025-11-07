--Rocky Gaucho
local s,id=GetID()
function s.initial_effect(c)
	--Sincro Genérico
	c:EnableReviveLimit()
	aux.AddSynchroProcedure(c,aux.FilterBoolFunction(Card.IsSetCard,0xc50),aux.NonTuner(nil),1)

	--Tratar como Nível 6 para Invocações-Sincro
	local e1=Effect.CreateEffect(c)
	e1:SetType(EFFECT_TYPE_SINGLE)
	e1:SetProperty(EFFECT_FLAG_SINGLE_RANGE)
	e1:SetCode(EFFECT_SYNCHRO_LEVEL)
	e1:SetRange(LOCATION_MZONE+LOCATION_HAND)
	e1:SetValue(s.slevel)
	c:RegisterEffect(e1)
end

--Função que define o valor do Nível para uso em Invocações-Sincro
function s.slevel(e,c)
	--Aqui o jogador escolhe se o monstro será tratado como Nível 5 ou 6
	Duel.Hint(HINT_SELECTMSG,e:GetHandlerPlayer(),aux.Stringid(id,0)) -- "Escolha o Nível para Invocação-Sincro"
	local op=Duel.SelectOption(e:GetHandlerPlayer(),aux.Stringid(id,1),aux.Stringid(id,2))
	--op = 0 → Nível 5 | op = 1 → Nível 6
	local lv=e:GetHandler():GetLevel()
	if op==1 then
		return (6<<16)|lv -- trata como 6 para fins de Sincro
	else
		return (5<<16)|lv -- trata como 5 para fins de Sincro
	end
end
